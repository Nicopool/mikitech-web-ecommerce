"""Vistas de la aplicación núcleo (core) de MIKITECH"""

import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from products.models import Producto, Categoria
from users.models import Perfil
from interactions.models import Reseña, Voto, Favorito


def inicio(petición):
    """Página de inicio con productos destacados. Las categorías vienen del context_processor cacheado."""
    productos_destacados = Producto.objects.filter(
        esta_activo=True, es_destacado=True
    ).select_related('categoria')[:8]

    contexto = {
        'productos_destacados': productos_destacados,
        'titulo_pagina': 'MIKITECH — Alta Tecnología y Rendimiento',
    }
    return render(petición, 'core/home.html', contexto)


def buscar(petición):
    """Vista de búsqueda centralizada con filtros y ordenamiento."""
    petición_get = petición.GET
    consulta = petición_get.get('q', '')
    enlace_categoría = petición_get.get('categoria', '')
    precio_min = petición_get.get('precio_min', '')
    precio_max = petición_get.get('precio_max', '')
    marca = petición_get.get('marca', '')
    orden = petición_get.get('orden', '-creado_el')

    productos = Producto.objects.filter(esta_activo=True).select_related('categoria')

    if consulta:
        productos = productos.filter(
            Q(nombre__icontains=consulta) |
            Q(descripcion__icontains=consulta) |
            Q(marca__icontains=consulta) |
            Q(modelo__icontains=consulta)
        )

    if enlace_categoría:
        productos = productos.filter(categoria__enlace=enlace_categoría)

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

    if marca:
        productos = productos.filter(marca__icontains=marca)

    # Ordenamiento
    ordenes_permitidos = {
        'precio_asc': 'precio',
        'precio_desc': '-precio',
        'nombre_asc': 'nombre',
        'nuevo': '-creado_el',
    }
    campo_orden = ordenes_permitidos.get(orden, '-creado_el')
    productos = productos.order_by(campo_orden)

    # Paginación (12 por página)
    per_pagina = 12
    param_pagina = petición_get.get('pagina') or petición_get.get('page') or '1'
    try:
        pagina = int(param_pagina)
        if pagina < 1:
            pagina = 1
    except ValueError:
        pagina = 1
    total = productos.count()
    inicio_p = (pagina - 1) * per_pagina
    fin_p = inicio_p + per_pagina
    productos_lista = productos[inicio_p:fin_p]
    total_paginas = (total + per_pagina - 1) // per_pagina

    from django.core.cache import cache
    categorías = cache.get('nav_categorias')
    if categorías is None:
        categorías = list(Categoria.objects.all().order_by('nombre'))
        cache.set('nav_categorias', categorías, 300)

    # Marcas cacheadas 10 minutos (cambian raramente)
    from django.core.cache import cache
    marcas = cache.get('marcas_activas')
    if marcas is None:
        marcas = list(
            Producto.objects.filter(esta_activo=True, marca__isnull=False)
            .values_list('marca', flat=True)
            .distinct().order_by('marca')
        )
        cache.set('marcas_activas', marcas, 600)

    current_category = None
    if enlace_categoría:
        try:
            current_category = Categoria.objects.get(enlace=enlace_categoría)
        except Categoria.DoesNotExist:
            pass

    contexto = {
        'productos': productos_lista,
        'query': consulta,
        'categorias': categorías,
        'marcas': [m for m in marcas if m],
        'enlace_categoria': enlace_categoría,
        'precio_min': precio_min,
        'precio_max': precio_max,
        'marca': marca,
        'orden': orden,
        'total': total,
        'pagina': pagina,
        'total_paginas': total_paginas,
        'current_category': current_category,
        'titulo_pagina': f'Búsqueda: {consulta}' if consulta else 'Catálogo de Productos',
        # Duplicados de compatibilidad (inglés/español)
        'products': productos_lista,
        'categories': categorías,
        'category_slug': enlace_categoría,
        'min_price': precio_min,
        'max_price': precio_max,
        'brand': marca,
        'sort': orden,
        'page': pagina,
        'total_pages': total_paginas,
    }
    return render(petición, 'core/search.html', contexto)


def perfil_publico(petición, nombre_usuario):
    """Perfil público de un usuario y sus interacciones."""
    perfil = get_object_or_404(Perfil, nombre_usuario=nombre_usuario)
    reseñas_usuario = Reseña.objects.filter(usuario=perfil, esta_aprobada=True).select_related('producto').order_by('-creado_el')[:10]
    favoritos_usuario = Favorito.objects.filter(usuario=perfil).select_related('producto').order_by('-creado_el')[:8]

    contexto = {
        'perfil': perfil,
        'reseñas': reseñas_usuario,
        'favoritos': favoritos_usuario,
        'titulo_pagina': f'Perfil de {perfil.nombre_mostrado}',
    }
    return render(petición, 'core/public_profile.html', contexto)


def agregar_al_carrito(petición, id_producto):
    """Añade un producto al carrito (acepta UUID o Slug) y redirige o responde JSON."""
    carrito = petición.session.get('cart', {})
    
    # Resolver id_producto (puede ser ID o Slug)
    from products.models import Producto
    import uuid
    
    producto_final = None
    try:
        # Intentar por UUID primero
        val_uuid = uuid.UUID(id_producto)
        producto_final = Producto.objects.get(id=val_uuid)
    except (ValueError, Producto.DoesNotExist):
        # Si falla, intentar por slug (enlace)
        try:
            producto_final = Producto.objects.get(enlace=id_producto)
        except Producto.DoesNotExist:
            pass

    if not producto_final:
        if petición.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'ok': False, 'error': 'Producto no encontrado'}, status=404)
        messages.error(petición, "Producto no encontrado.")
        return redirect('products:catalog')

    # Obtener la cantidad (por defecto 1)
    cantidad = 1
    cantidad_str = petición.POST.get('cantidad') or petición.GET.get('cantidad')
    if cantidad_str:
        try:
            cantidad = int(cantidad_str)
            if cantidad < 1:
                cantidad = 1
        except ValueError:
            pass

    id_str = str(producto_final.id)
    carrito[id_str] = carrito.get(id_str, 0) + cantidad
    petición.session['cart'] = carrito
    petición.session.modified = True
    
    if petición.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.http import JsonResponse
        total_items = sum(carrito.values())
        return JsonResponse({'ok': True, 'total_items': total_items})
    
    messages.success(petición, f"Agregado: {producto_final.nombre} ({cantidad} uds)")
    return redirect('core:cart')


def eliminar_del_carrito(petición, id_producto):
    """Elimina un producto del carrito de la sesión."""
    carrito = petición.session.get('cart', {})
    id_str = str(id_producto)
    if id_str in carrito:
        del carrito[id_str]
    petición.session['cart'] = carrito
    petición.session.modified = True
    
    if petición.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.http import JsonResponse
        return JsonResponse({'ok': True, 'eliminado': True})
    return redirect('core:cart')


def actualizar_carrito(petición, id_producto):
    """Actualiza la cantidad de un producto en el carrito (AJAX)."""
    from django.http import JsonResponse
    if petición.method == 'POST':
        carrito = petición.session.get('cart', {})
        id_str = str(id_producto)
        accion = petición.POST.get('accion', '')
        
        if id_str in carrito:
            if accion == 'sumar':
                carrito[id_str] += 1
            elif accion == 'restar':
                carrito[id_str] -= 1
                if carrito[id_str] <= 0:
                    del carrito[id_str]
        
        petición.session['cart'] = carrito
        petición.session.modified = True
        
        cantidad_item = carrito.get(id_str, 0)
        total_items = sum(carrito.values())
        
        # Respuesta AJAX rápida: solo devolver cantidad nueva
        # Los cálculos de precio se hacen en JavaScript (sin consultar DB)
        if petición.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'ok': True,
                'cantidad': cantidad_item,
                'total_items': total_items,
                'eliminado': id_str not in carrito,
            })
    return redirect('core:cart')


def _obtener_datos_carrito(petición):
    """Función interna que calcula los datos del carrito."""
    from decimal import Decimal
    carrito_sesion = petición.session.get('cart', {})
    artículos = []
    subtotal = Decimal('0')
    
    if carrito_sesion:
        # Filtrar solo claves que parezcan UUIDs válidos para evitar errores de base de datos
        valid_ids = []
        for k in carrito_sesion.keys():
            try:
                uuid.UUID(k)
                valid_ids.append(k)
            except ValueError:
                continue

        productos = Producto.objects.filter(id__in=valid_ids)
        for producto in productos:
            cantidad = carrito_sesion.get(str(producto.id), 0)
            precio_final = producto.precio_con_descuento
            total_línea = precio_final * cantidad
            artículos.append({
                'producto': producto,
                'cantidad': cantidad,
                'total_linea': total_línea,
            })
            subtotal += total_línea
    
    # El IVA (19%) ya viene incluido en el precio de los productos
    iva = subtotal - (subtotal / Decimal('1.19'))
    total = subtotal
    total_articulos = sum(carrito_sesion.values()) if carrito_sesion else 0
    
    return {
        'articulos': artículos,
        'subtotal': subtotal,
        'iva': iva,
        'total': total,
        'total_articulos': total_articulos,
    }


def ver_carrito(petición):
    """Página de revisión del carrito ANTES de ir al checkout."""
    datos = _obtener_datos_carrito(petición)
    contexto = {
        **datos,
        'titulo_pagina': 'Tu Carrito — MIKITECH',
    }
    return render(petición, 'core/cart.html', contexto)


def cart_status_api(petición):
    """Retorna el estado del carrito en formato JSON para el Mini-Carrito Drawer."""
    from django.http import JsonResponse
    from core.templatetags.miki_filters import currency_cop
    
    datos = _obtener_datos_carrito(petición)
    
    articulos_json = []
    for item in datos['articulos']:
        prod = item['producto']
        precio_final = prod.precio_con_descuento if prod.descuento_activo else prod.precio
        articulos_json.append({
            'producto': {
                'id': str(prod.id),
                'nombre': prod.nombre,
                'url_imagen': prod.url_imagen_principal,
                'descuento_activo': prod.descuento_activo,
                'porcentaje': prod.descuento_porcentaje if prod.descuento_activo else 0,
                'existencias': prod.existencias,
            },
            'cantidad': item['cantidad'],
            'total_linea': float(item['total_linea']),
            'precio_formateado': currency_cop(precio_final),
        })
    
    return JsonResponse({
        'total_articulos': datos['total_articulos'],
        'total_bruto': float(datos['total']),
        'total_formateado': currency_cop(datos['total']),
        'articulos': articulos_json
    })


def carrito(petición):
    """Finalización de compra (checkout) con formulario de pago."""
    if not petición.session.get('usuario_id'):
        messages.warning(petición, "Para finalizar tu compra, por favor inicia sesión.")
        return redirect('/cuenta/ingreso/?next=/checkout/')

    datos = _obtener_datos_carrito(petición)
    
    if not datos['articulos']:
        return redirect('core:cart')

    if petición.method == 'POST':
        from interactions.models import Pedido, DetallePedido
        from django.db import transaction

        usuario_id = petición.session.get('usuario_id')
        direccion = petición.POST.get('address', '') + ', ' + petición.POST.get('city', '') + ' ' + petición.POST.get('zip', '')
        metodo = petición.POST.get('metodo_pago', 'tarjeta')
        estado = 'pending' if metodo == 'efectivo' else 'processing'

        cedula_id = petición.POST.get('cedula', '')
        telefono = petición.POST.get('telefono', '')

        with transaction.atomic():
            pedido = Pedido.objects.create(
                usuario_id=usuario_id,
                estado=estado,
                monto_total=datos['total'],
                direccion_envio=direccion,
                cedula=cedula_id,
                telefono=telefono,
                notas=f"Método de pago: {metodo.upper()}"
            )

            # Crear todos los detalles de una sola vez (bulk_create)
            detalles = []
            productos_actualizar = []
            for item in datos['articulos']:
                detalles.append(DetallePedido(
                    pedido=pedido,
                    producto=item['producto'],
                    cantidad=item['cantidad'],
                    precio_unitario=item['producto'].precio_con_descuento
                ))
                prod = item['producto']
                prod.existencias = max(0, prod.existencias - item['cantidad'])
                productos_actualizar.append(prod)

            DetallePedido.objects.bulk_create(detalles)
            if productos_actualizar:
                Producto.objects.bulk_update(productos_actualizar, ['existencias'])

            # Notificar al cliente
            from users.models import Notificacion
            Notificacion.objects.create(
                id=uuid.uuid4(),
                usuario_id=usuario_id,
                mensaje=f"[Orden Recibida] ¡Hola! Hemos recibido tu pedido #{str(pedido.id)[:8]}. Pronto comenzaremos con el alistamiento técnico.",
            )
        
        petición.session['cart'] = {}
        petición.session.modified = True
        return render(petición, 'core/checkout.html', {
            'exito': True, 
            'titulo_pagina': 'Compra Exitosa — MIKITECH'
        })

    contexto = {
        **datos,
        'titulo_pagina': 'Finalizar Compra — MIKITECH',
    }
    return render(petición, 'core/checkout.html', contexto)



def contacto(petición):
    """Formulario de contacto básico."""
    if petición.method == 'POST':
        messages.success(petición, "Tu mensaje ha sido enviado. Nos contactaremos pronto.")
        return redirect('core:contact')
    return render(petición, 'core/contact.html', {'titulo_pagina': 'Contacto — MIKITECH'})


def blog(petición):
    """Próximamente: Blog de tecnología."""
    return render(petición, 'core/blog.html', {'titulo_pagina': 'Blog — MIKITECH'})


def puerta_administrador(petición):
    """Página intermedia para acceso administrativo."""
    return redirect('core:admin_gateway') # Redirección a la vista en admin_views para consistencia


def ping(petición):
    """Endpoint simple para pruebas de carga con k6."""
    from django.http import JsonResponse
    return JsonResponse({'status': 'ok', 'msg': 'pong'})


