"""Vistas de la aplicación productos — catálogo y detalles — MIKITECH"""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q
from .models import Categoria, Producto


def lista_productos(petición):
    """Vista principal del catálogo con búsqueda y filtros."""
    from django.db.models import Avg
    from django.utils import timezone

    consulta = petición.GET.get('q', '')
    id_categoría = petición.GET.get('categoria', '')
    precio_min = petición.GET.get('precio_min', '')
    precio_max = petición.GET.get('precio_max', '')
    marcas_seleccionadas = petición.GET.getlist('marca')
    calificacion_min = petición.GET.get('calificacion', '')
    solo_stock = petición.GET.get('stock') == 'true'
    solo_ofertas = petición.GET.get('oferta') == 'true'
    ordenar_por = petición.GET.get('orden', '-creado_el')

    # Annotate with Avg rating so we can filter by it in SQL
    productos = Producto.objects.filter(esta_activo=True).select_related('categoria').annotate(
        calificacion_promedio_db=Avg('reseñas__calificacion')
    )

    # Búsqueda por texto
    if consulta:
        productos = productos.filter(
            Q(nombre__icontains=consulta) |
            Q(descripcion__icontains=consulta) |
            Q(marca__icontains=consulta) |
            Q(modelo__icontains=consulta)
        )

    # Filtrar por categoría (acepta UUID o slug)
    if id_categoría:
        import uuid
        try:
            uuid.UUID(id_categoría)
            productos = productos.filter(categoria_id=id_categoría)
        except ValueError:
            productos = productos.filter(categoria__enlace=id_categoría)

    # Filtrar por precio
    if precio_min:
        try:
            productos = productos.filter(precio__gte=float(precio_min))
        except ValueError:
            pass
    if precio_max:
        try:
            productos = productos.filter(precio__lte=float(precio_max))
        except ValueError:
            pass

    # Filtrar por marcas
    if marcas_seleccionadas:
        marcas_filtradas = [m for m in marcas_seleccionadas if m]
        if marcas_filtradas:
            productos = productos.filter(marca__in=marcas_filtradas)

    # Filtrar por calificación mínima
    if calificacion_min:
        try:
            productos = productos.filter(calificacion_promedio_db__gte=float(calificacion_min))
        except ValueError:
            pass

    # Filtrar por stock disponible
    if solo_stock:
        productos = productos.filter(existencias__gt=0)

    # Filtrar por ofertas activas
    if solo_ofertas:
        productos = productos.filter(
            Q(descuento_porcentaje__gt=0) &
            (Q(descuento_expira_el__isnull=True) | Q(descuento_expira_el__gt=timezone.now()))
        )

    # Ordenar
    mapeo_orden = {
        'precio_asc': 'precio',
        'precio_desc': '-precio',
        'nombre_asc': 'nombre',
        'nuevo': '-creado_el',
    }
    campo_orden = mapeo_orden.get(ordenar_por, '-creado_el')
    productos = productos.order_by(campo_orden)

    # Paginación (12 por página)
    paginador = Paginator(productos, 12)
    param_pagina = petición.GET.get('pagina') or petición.GET.get('page') or '1'
    try:
        numero_pagina = int(param_pagina)
        if numero_pagina < 1:
            numero_pagina = 1
    except ValueError:
        numero_pagina = 1
    objetos_pagina = paginador.get_page(numero_pagina)

    from django.core.cache import cache
    categorías = cache.get('nav_categorias')
    if categorías is None:
        categorías = list(Categoria.objects.all().order_by('nombre'))
        cache.set('nav_categorias', categorías, 300)

    # Obtener marcas disponibles dinámicamente
    marcas_disponibles = list(
        Producto.objects.filter(esta_activo=True)
        .exclude(marca__isnull=True)
        .exclude(marca='')
        .values_list('marca', flat=True)
        .distinct()
        .order_by('marca')
    )

    # Ofertas del día (los 3 productos activos con mayores descuentos)
    ofertas_del_dia = list(
        Producto.objects.filter(esta_activo=True, descuento_porcentaje__gt=0)
        .filter(Q(descuento_expira_el__isnull=True) | Q(descuento_expira_el__gt=timezone.now()))
        .order_by('-descuento_porcentaje')[:3]
    )

    # Más vendidos (los 5 productos con más vistas o destacados)
    mas_vendidos = list(
        Producto.objects.filter(esta_activo=True).order_by('-conteo_vistas')[:5]
    )

    # Categoría actual objeto (para breadcrumbs)
    categoria_actual_obj = None
    if id_categoría:
        import uuid
        try:
            uuid.UUID(id_categoría)
            categoria_actual_obj = Categoria.objects.filter(id=id_categoría).first()
        except ValueError:
            categoria_actual_obj = Categoria.objects.filter(enlace=id_categoría).first()

    contexto = {
        'productos': objetos_pagina,
        'categorias': categorías,
        'marcas_disponibles': marcas_disponibles,
        'marcas_seleccionadas': marcas_seleccionadas,
        'calificacion_min': calificacion_min,
        'solo_stock': solo_stock,
        'solo_ofertas': solo_ofertas,
        'ofertas_del_dia': ofertas_del_dia,
        'mas_vendidos': mas_vendidos,
        'categoria_actual_obj': categoria_actual_obj,
        'query': consulta,
        'categoria_actual': id_categoría,
        'precio_min': precio_min,
        'precio_max': precio_max,
        'orden': ordenar_por,
        'titulo_pagina': 'Catálogo de Tecnología — MIKITECH',
    }

    return render(petición, 'products/catalog_public.html', contexto)


def detalle_producto(petición, enlace):
    """Vista de detalle de un producto específico."""
    producto = get_object_or_404(Producto, enlace=enlace, esta_activo=True)
    
    # Incrementar contador de vistas (SQL directo, sin save() completo)
    Producto.objects.filter(id=producto.id).update(
        conteo_vistas=models.F('conteo_vistas') + 1
    )

    # Productos relacionados (misma categoría, excluyendo el actual)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        esta_activo=True
    ).exclude(id=producto.id)[:4]

    # Verificar si el usuario ya votó
    usuario_id = petición.session.get('usuario_id')
    ha_votado = False
    
    if usuario_id:
        from interactions.models import Voto
        from users.models import Perfil
        try:
            perfil = Perfil.objects.get(id=usuario_id)
            ha_votado = Voto.objects.filter(usuario=perfil, producto=producto).exists()
        except Perfil.DoesNotExist:
            pass

    contexto = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'ha_votado': ha_votado,
        'titulo_pagina': f'{producto.nombre} | MIKITECH',
    }

    return render(petición, 'products/detail.html', contexto)
