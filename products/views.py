"""Vistas de la aplicación productos — catálogo y detalles — MIKITECH"""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q
from .models import Categoria, Producto


def lista_productos(petición):
    """Vista principal del catálogo con búsqueda y filtros."""
    consulta = petición.GET.get('q', '')
    id_categoría = petición.GET.get('categoria', '')
    precio_min = petición.GET.get('precio_min', '')
    precio_max = petición.GET.get('precio_max', '')
    ordenar_por = petición.GET.get('orden', '-creado_el')

    productos = Producto.objects.filter(esta_activo=True)

    # Búsqueda por texto
    if consulta:
        productos = productos.filter(
            Q(nombre__icontains=consulta) |
            Q(descripcion__icontains=consulta) |
            Q(marca__icontains=consulta) |
            Q(modelo__icontains=consulta)
        )

    # Filtrar por categoría
    if id_categoría:
        productos = productos.filter(categoria_id=id_categoría)

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
    numero_pagina = petición.GET.get('pagina', 1)
    objetos_pagina = paginador.get_page(numero_pagina)

    categorías = Categoria.objects.all().order_by('nombre')

    contexto = {
        'productos': objetos_pagina,
        'categorias': categorías,
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

    # Verificar si el usuario ya votó o marcó como favorito
    usuario_id = petición.session.get('usuario_id')
    ha_votado = False
    es_favorito = False
    
    if usuario_id:
        from interactions.models import Voto, Favorito
        from users.models import Perfil
        try:
            perfil = Perfil.objects.get(id=usuario_id)
            ha_votado = Voto.objects.filter(usuario=perfil, producto=producto).exists()
            es_favorito = Favorito.objects.filter(usuario=perfil, producto=producto).exists()
        except Perfil.DoesNotExist:
            pass

    from interactions.models import Reseña
    reseñas = Reseña.objects.filter(producto=producto).select_related('usuario').order_by('-creado_el')

    contexto = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'reseñas': reseñas,
        'ha_votado': ha_votado,
        'es_favorito': es_favorito,
        'titulo_pagina': f'{producto.nombre} | MIKITECH',
    }

    return render(petición, 'products/detail.html', contexto)
