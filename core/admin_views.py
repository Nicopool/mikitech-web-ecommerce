"""Vistas del panel administrativo con gateway SENA-2026 — MIKITECH"""

import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Producto, Categoria
from interactions.models import Reseña, Pedido
from users.models import Perfil, Notificacion
import os
from django.core.files.storage import default_storage


from functools import wraps

CODIGO_ADMIN = getattr(settings, 'ADMIN_GATEWAY_CODE', 'SENA-2026')


def requerir_administrador(función_vista):
    """Decorador que requiere rol admin (administrador)."""
    @wraps(función_vista)
    def envoltura(petición, *args, **kwargs):
        if not petición.session.get('usuario_id') or petición.session.get('rol_usuario') != 'admin':
            return redirect('core:admin_gateway') if 'core' in petición.resolver_match.namespaces else redirect('/admin-panel/pasarela/')
        return función_vista(petición, *args, **kwargs)
    return envoltura


def pasarela(petición):
    """Pasarela de seguridad inicial solicitando el código SENA-2026."""
    # Si ya está logueado como admin, ir directo al panel
    if petición.session.get('rol_usuario') == 'admin':
        return redirect('/admin-panel/')

    # Si NO hay sesión de admin activa, limpiar la pasarela para forzar el código siempre
    if not petición.session.get('usuario_id'):
        if 'pasarela_administrador_superada' in petición.session:
            del petición.session['pasarela_administrador_superada']
            petición.session.modified = True

    if petición.session.get('pasarela_administrador_superada'):
        return redirect('/admin-panel/login/')

    if petición.method == 'POST':
        codigo_enviado = petición.POST.get('codigo_secreto', '').strip()
        if codigo_enviado == CODIGO_ADMIN:
            petición.session['pasarela_administrador_superada'] = True
            petición.session.modified = True
            return redirect('/admin-panel/login/')
        return render(petición, 'admin_panel/gateway.html', {
            'error': 'Código de acceso incorrecto.',
            'titulo_pagina': 'Acceso Restringido — MIKITECH',
        })

    return render(petición, 'admin_panel/gateway.html', {
        'titulo_pagina': 'Acceso Restringido — MIKITECH',
    })



def login_administrador(petición):
    """Inicio de sesión exclusivo para administradores."""
    if not petición.session.get('pasarela_administrador_superada'):
        return redirect('/admin-panel/pasarela/')

    if petición.session.get('rol_usuario') == 'admin':
        return redirect('/admin-panel/')

    if petición.method == 'POST':
        from users.supabase_auth import iniciar_sesion_usuario # Asumiendo traducción en users/supabase_auth.py
        correo = petición.POST.get('correo', '').strip()
        clave = petición.POST.get('clave', '')

        datos, error = iniciar_sesion_usuario(correo, clave)

        if error:
            return render(petición, 'admin_panel/login.html', {
                'error': 'Credenciales incorrectas o acceso denegado.',
                'correo': correo,
                'titulo_pagina': 'Login Administrador — MIKITECH',
            })

        id_usuario = datos.get('user', {}).get('id')
        try:
            perfil = Perfil.objects.get(id=id_usuario)
            if not perfil.es_administrador:
                return render(petición, 'admin_panel/login.html', {
                    'error': 'No posees permisos de administrador.',
                    'titulo_pagina': 'Login Administrador — MIKITECH',
                })
            petición.session['usuario_id'] = id_usuario
            petición.session['token_acceso'] = datos.get('access_token')
            petición.session['rol_usuario'] = 'admin'
            petición.session['nombre_usuario'] = perfil.nombre_usuario
            petición.session['avatar_url'] = perfil.url_avatar or ''
            petición.session.modified = True
            return redirect('/admin-panel/')
        except Perfil.DoesNotExist:
            return render(petición, 'admin_panel/login.html', {
                'error': 'Perfil de administrador no encontrado en la base de datos.',
                'titulo_pagina': 'Login Administrador — MIKITECH',
            })

    return render(petición, 'admin_panel/login.html', {
        'titulo_pagina': 'Login Administrador — MIKITECH',
    })


def registro_administrador(petición):
    """Registro de nuevos administradores (requiere pasar pasarela)."""
    if not petición.session.get('pasarela_administrador_superada'):
        return redirect('/admin-panel/pasarela/')

    if petición.session.get('rol_usuario') == 'admin':
        return redirect('/admin-panel/')

    if petición.method == 'POST':
        from users.supabase_auth import registrar_usuario
        nombre_completo = petición.POST.get('nombre_completo', '').strip()
        nombre_usuario = petición.POST.get('nombre_usuario', '').strip()
        correo = petición.POST.get('correo', '').strip()
        clave = petición.POST.get('clave', '')
        confirmar_clave = petición.POST.get('confirmar_clave', '')

        contexo = {
            'nombre_completo': nombre_completo,
            'nombre_usuario': nombre_usuario,
            'correo': correo,
            'titulo_pagina': 'Registro Administrador — MIKITECH',
        }

        if not all([nombre_completo, nombre_usuario, correo, clave]):
            contexo['error'] = 'Por favor completa todos los campos del formulario.'
            return render(petición, 'admin_panel/register.html', contexo)

        if clave != confirmar_clave:
            contexo['error'] = 'Las contraseñas no coinciden.'
            return render(petición, 'admin_panel/register.html', contexo)

        if len(clave) < 6:
            contexo['error'] = 'La contraseña debe tener al menos 6 caracteres.'
            return render(petición, 'admin_panel/register.html', contexo)

        if Perfil.objects.filter(nombre_usuario=nombre_usuario).exists():
            contexo['error'] = 'Ese nombre de usuario ya está registrado.'
            return render(petición, 'admin_panel/register.html', contexo)

        datos, error = registrar_usuario(correo, clave, nombre_completo, nombre_usuario, rol='admin')

        if error:
            contexo['error'] = f'Error en el registro: {error}'
            return render(petición, 'admin_panel/register.html', contexo)

        # Bypass the Supabase Email Confirmation locally for admin signups
        try:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE auth.users SET email_confirmed_at = NOW() WHERE email = %s", 
                    [correo]
                )
        except Exception as e:
            print("No se pudo saltar la confirmación de correo:", e)

        return render(petición, 'admin_panel/login.html', {
            'success': 'Cuenta de administrador creada y verificada automáticamente. Ya puedes iniciar sesión.',
            'titulo_pagina': 'Login Administrador — MIKITECH'
        })

    return render(petición, 'admin_panel/register.html', {
        'titulo_pagina': 'Registro Administrador — MIKITECH',
    })


def cerrar_sesion_administrador(petición):
    """Cierra la sesión y limpia el rastro de la pasarela."""
    petición.session.flush()
    return redirect('/admin-panel/pasarela/')


@requerir_administrador
def tablero_administrador(petición):
    """Estadísticas principales del panel."""
    from django.db.models import Sum, F
    valor_total_inv = Producto.objects.aggregate(total=Sum(F('precio') * F('existencias')))['total'] or 0
    ingresos_estimados = Pedido.objects.filter(estado__in=['delivered', 'shipped']).aggregate(total=Sum('monto_total'))['total'] or 0
    
    estadísticas = {
        'total_productos': Producto.objects.count(),
        'productos_activos': Producto.objects.filter(esta_activo=True).count(),
        'total_categorias': Categoria.objects.count(),
        'total_usuarios': Perfil.objects.count(),
        'total_resenas': Reseña.objects.count(),
        'stock_bajo': Producto.objects.filter(existencias__lte=5, esta_activo=True).count(),
        'valor_total_inventario': valor_total_inv,
        'ingresos_estimados': ingresos_estimados,
    }
    productos_recientes = Producto.objects.order_by('-creado_el')[:5]
    reseñas_recientes = Reseña.objects.select_related('producto', 'usuario').order_by('-creado_el')[:5]

    return render(petición, 'admin_panel/dashboard.html', {
        'estadisticas': estadísticas,
        'productos_recientes': productos_recientes,
        'resenas_recientes': reseñas_recientes,
        'titulo_pagina': 'Tablero de Control — MIKITECH',
    })


@requerir_administrador
def gestion_productos(petición):
    """Lista de productos para gestión administrativa."""
    productos = Producto.objects.select_related('categoria').order_by('-creado_el')
    
    from django.db.models import Sum, F
    valor_total_inv = productos.aggregate(total=Sum(F('precio') * F('existencias')))['total'] or 0
    
    return render(petición, 'admin_panel/products.html', {
        'productos': productos,
        'valor_total_inventario': valor_total_inv,
        'titulo_pagina': 'Gestión de Productos — MIKITECH',
    })


@requerir_administrador
def crear_producto(petición):
    """Procesamiento y vista para la creación de nuevos productos."""
    categorías = Categoria.objects.all().order_by('nombre')
    if petición.method == 'POST':
        nombre = petición.POST.get('nombre', '').strip()
        id_categoria = petición.POST.get('id_categoria', '')
        precio = petición.POST.get('precio', '0')
        existencias = petición.POST.get('existencias', '0')
        marca = petición.POST.get('marca', '').strip()
        descripcion = petición.POST.get('descripcion', '').strip()
        descripcion_corta = petición.POST.get('descripcion_corta', '').strip()
        es_destacado = petición.POST.get('es_destacado') == 'on'
        descuento_porcentaje = int(petición.POST.get('descuento_porcentaje', '0') or '0')
        descuento_expira_str = petición.POST.get('descuento_expira_el', '').strip()
        descuento_expira_el = None
        if descuento_expira_str:
            from django.utils import timezone
            from datetime import datetime
            try:
                descuento_expira_el = datetime.fromisoformat(descuento_expira_str).astimezone(timezone.utc)
            except ValueError:
                pass

        if nombre:
            from django.utils.text import slugify
            base_enlace = slugify(nombre)
            enlace = base_enlace
            contador = 1
            while Producto.objects.filter(enlace=enlace).exists():
                enlace = f"{base_enlace}-{contador}"
                contador += 1

            try:
                cat = Categoria.objects.get(id=id_categoria)
                Producto.objects.create(
                    id=uuid.uuid4(),
                    categoria=cat,
                    nombre=nombre,
                    enlace=enlace,
                    precio=float(precio),
                    existencias=int(existencias),
                    marca=marca,
                    descripcion=descripcion,
                    descripcion_corta=descripcion_corta,
                    url_imagen_principal=petición.POST.get('url_imagen_principal', '').strip(),
                    es_destacado=es_destacado,
                    descuento_porcentaje=descuento_porcentaje,
                    descuento_expira_el=descuento_expira_el,
                    esta_activo=True,
                )
                
                # Procesar Archivo Local después de crear para tener el ID si es necesario, 
                # aunque aquí usamos UUID para el nombre del archivo.
                if 'archivo_imagen' in petición.FILES:
                    archivo = petición.FILES['archivo_imagen']
                    nombre_unico = f"products/{uuid.uuid4()}{os.path.splitext(archivo.name)[1]}"
                    ruta_guardada = default_storage.save(nombre_unico, archivo)
                    # Re-obtener y actualizar el producto
                    prod_reciente = Producto.objects.filter(enlace=enlace).first()
                    if prod_reciente:
                        prod_reciente.url_imagen_principal = f"{settings.MEDIA_URL}{ruta_guardada}"
                        prod_reciente.save()
                messages.success(petición, f'Producto "{nombre}" creado con éxito.')
                return redirect('/admin-panel/productos/')
            except Exception as e:
                return render(petición, 'admin_panel/product_form.html', {
                    'categorias': categorías,
                    'error': f'Error al guardar el producto: {str(e)}',
                    'titulo_pagina': 'Crear Producto — MIKITECH',
                })

    return render(petición, 'admin_panel/product_form.html', {
        'categorias': categorías,
        'titulo_pagina': 'Crear Producto — MIKITECH',
    })


@requerir_administrador
def editar_producto(petición, id_producto):
    """Formulario para la edición de productos existentes."""
    producto = get_object_or_404(Producto, id=id_producto)
    categorías = Categoria.objects.all().order_by('nombre')
    if petición.method == 'POST':
        producto.nombre = petición.POST.get('nombre', producto.nombre).strip()
        producto.precio = float(petición.POST.get('precio', producto.precio))
        producto.existencias = int(petición.POST.get('existencias', producto.existencias))
        producto.marca = petición.POST.get('marca', producto.marca)
        producto.descripcion = petición.POST.get('descripcion', producto.descripcion)
        producto.descripcion_corta = petición.POST.get('descripcion_corta', producto.descripcion_corta)
        
        # Procesar Archivo Local si existe
        if 'archivo_imagen' in petición.FILES:
            archivo = petición.FILES['archivo_imagen']
            nombre_unico = f"products/{uuid.uuid4()}{os.path.splitext(archivo.name)[1]}"
            ruta_guardada = default_storage.save(nombre_unico, archivo)
            producto.url_imagen_principal = f"{settings.MEDIA_URL}{ruta_guardada}"
        else:
            producto.url_imagen_principal = petición.POST.get('url_imagen_principal', producto.url_imagen_principal).strip()
        producto.es_destacado = petición.POST.get('es_destacado') == 'on'
        producto.esta_activo = petición.POST.get('esta_activo') == 'on'
        # Descuento
        producto.descuento_porcentaje = int(petición.POST.get('descuento_porcentaje', '0') or '0')
        desc_exp_str = petición.POST.get('descuento_expira_el', '').strip()
        if desc_exp_str:
            from django.utils import timezone
            from datetime import datetime
            try:
                producto.descuento_expira_el = datetime.fromisoformat(desc_exp_str).astimezone(timezone.utc)
            except ValueError:
                producto.descuento_expira_el = None
        else:
            producto.descuento_expira_el = None
        id_cat = petición.POST.get('id_categoria')
        if id_cat:
            try:
                producto.categoria = Categoria.objects.get(id=id_cat)
            except Categoria.DoesNotExist:
                pass
        producto.save()
        messages.success(petición, f'Cambios en "{producto.nombre}" guardados.')
        return redirect('/admin-panel/productos/')

    return render(petición, 'admin_panel/product_form.html', {
        'producto': producto,
        'categorias': categorías,
        'titulo_pagina': f'Editar: {producto.nombre} — MIKITECH',
    })


@requerir_administrador
@require_POST
def eliminar_producto(petición, id_producto):
    """Proceso de eliminación física de un producto."""
    producto = get_object_or_404(Producto, id=id_producto)
    nombre = producto.nombre
    producto.delete()
    messages.success(petición, f'Producto "{nombre}" eliminado satisfactoriamente.')
    return redirect('/admin-panel/productos/')


@requerir_administrador
def gestion_categorias(petición):
    """Visualización y control de las categorías del catálogo."""
    categorías = Categoria.objects.all().order_by('nombre')
    return render(petición, 'admin_panel/categories.html', {
        'categorias': categorías,
        'titulo_pagina': 'Gestión de Categorías — MIKITECH',
    })


@requerir_administrador
def crear_categoria(petición):
    """Añadir nuevas agrupaciones de productos."""
    if petición.method == 'POST':
        from django.utils.text import slugify
        nombre = petición.POST.get('nombre', '').strip()
        descripcion = petición.POST.get('descripcion', '').strip()
        icono = petición.POST.get('icono', '').strip()
        url_imagen = petición.POST.get('url_imagen', '').strip()
        
        # Procesar Archivo Local si existe
        if 'archivo_imagen' in petición.FILES:
            archivo = petición.FILES['archivo_imagen']
            nombre_unico = f"categories/{uuid.uuid4()}{os.path.splitext(archivo.name)[1]}"
            ruta_guardada = default_storage.save(nombre_unico, archivo)
            url_imagen = f"{settings.MEDIA_URL}{ruta_guardada}"
        
        if not nombre:
            return render(petición, 'admin_panel/category_form.html', {
                'error': 'El nombre de la categoría es obligatorio.',
                'titulo_pagina': 'Crear Categoría — MIKITECH'
            })

        base_enlace = slugify(nombre)
        enlace = base_enlace
        contador = 1
        while Categoria.objects.filter(enlace=enlace).exists():
            enlace = f"{base_enlace}-{contador}"
            contador += 1

        try:
            Categoria.objects.create(
                nombre=nombre, 
                enlace=enlace, 
                descripcion=descripcion, 
                icono=icono,
                url_imagen=url_imagen
            )
            messages.success(petición, f'Categoría "{nombre}" establecida.')
            return redirect('/admin-panel/categorias/')
        except Exception as e:
            return render(petición, 'admin_panel/category_form.html', {
                'error': f'Imposible crear categoría: {str(e)}',
                'titulo_pagina': 'Crear Categoría — MIKITECH'
            })

    return render(petición, 'admin_panel/category_form.html', {'titulo_pagina': 'Crear Categoría — MIKITECH'})


@requerir_administrador
def editar_categoria(petición, id_cat):
    """Modificar propiedades de una categoría existente."""
    categoría = get_object_or_404(Categoria, id=id_cat)
    if petición.method == 'POST':
        categoría.nombre = petición.POST.get('nombre', categoría.nombre).strip()
        categoría.descripcion = petición.POST.get('descripcion', categoría.descripcion).strip()
        categoría.icono = petición.POST.get('icono', categoría.icono).strip()
        
        # Procesar Archivo Local si existe
        if 'archivo_imagen' in petición.FILES:
            archivo = petición.FILES['archivo_imagen']
            nombre_unico = f"categories/{uuid.uuid4()}{os.path.splitext(archivo.name)[1]}"
            ruta_guardada = default_storage.save(nombre_unico, archivo)
            categoría.url_imagen = f"{settings.MEDIA_URL}{ruta_guardada}"
        else:
            categoría.url_imagen = petición.POST.get('url_imagen', categoría.url_imagen).strip()
        categoría.save()
        messages.success(petición, f'Categoría "{categoría.nombre}" actualizada.')
        return redirect('/admin-panel/categorias/')
    return render(petición, 'admin_panel/category_form.html', {
        'categoria': categoría,
        'titulo_pagina': f'Cat: {categoría.nombre} — MIKITECH',
    })


@requerir_administrador
@require_POST
def eliminar_categoria(petición, id_cat):
    """Remover categorías si están vacías o bajo confirmación."""
    categoría = get_object_or_404(Categoria, id=id_cat)
    try:
        nombre = categoría.nombre
        categoría.delete()
        messages.success(petición, f'Categoría "{nombre}" removida.')
    except Exception as e:
        messages.error(petición, f'Fallo en borrado: {str(e)}.')
    
    return redirect('/admin-panel/categorias/')


@requerir_administrador
def gestion_usuarios(petición):
    """Monitorización de perfiles de clientes y administradores."""
    usuarios = Perfil.objects.prefetch_related(
        'pedidos__detalles__producto',
        'reseñas__producto'
    ).all().order_by('-creado_el')
    conteo_admin = usuarios.filter(rol='admin').count()
    conteo_cliente = usuarios.filter(rol='client').count()
    return render(petición, 'admin_panel/users.html', {
        'usuarios': usuarios,
        'conteo_admin': conteo_admin,
        'conteo_cliente': conteo_cliente,
        'titulo_pagina': 'Gestión de Usuarios — MIKITECH',
    })


@requerir_administrador
def moderacion_resenas(petición):
    """Panel de moderación para comentarios de productos."""
    reseñas = Reseña.objects.select_related('producto', 'usuario').order_by('-creado_el')
    return render(petición, 'admin_panel/reviews.html', {
        'resenas': reseñas,
        'titulo_pagina': 'Moderación de Reseñas — MIKITECH',
    })


@requerir_administrador
@require_POST
def eliminar_resena(petición, id_resena):
    """Eliminar un comentario inapropiado o falso."""
    reseña = get_object_or_404(Reseña, id=id_resena)
    reseña.delete()
    messages.success(petición, 'Reseña eliminada con éxito.')
    return redirect('/admin-panel/resenas/')


@requerir_administrador
@require_POST
def enviar_notificacion_resena(petición, id_resena):
    """Enviar un aviso de moderación al usuario de la reseña."""
    reseña = get_object_or_404(Reseña, id=id_resena)
    mensaje = petición.POST.get('mensaje', '').strip()
    
    if not mensaje:
        messages.error(petición, 'Debes escribir un mensaje para la notificación.')
        return redirect('/admin-panel/resenas/')
    
    try:
        Notificacion.objects.create(
            id=uuid.uuid4(),
            usuario=reseña.usuario,
            mensaje=f"Aviso de Moderación MIKITECH: {mensaje} (Ref: {reseña.producto.nombre})",
        )
        messages.success(petición, f'Notificación enviada a {reseña.usuario.nombre_usuario}.')
    except Exception as e:
        messages.error(petición, f'Error al enviar notificación: {str(e)}')
        
    return redirect('/admin-panel/resenas/')


@requerir_administrador
def reportes_dashboard(petición):
    """Métricas globales y reportes exportables con filtros de tiempo dinámicos."""
    import datetime
    from django.utils import timezone
    from django.db.models import Sum, Count, Avg, F
    from django.db.models.functions import TruncMonth
    
    dias = petición.GET.get('dias', 'all')
    filtro_fecha = {}
    filtro_fecha_usuario = {}
    
    if dias.isdigit():
        fecha_limite = timezone.now() - datetime.timedelta(days=int(dias))
        filtro_fecha = {'creado_el__gte': fecha_limite}
        filtro_fecha_usuario = {'creado_el__gte': fecha_limite}

    # Estadísticas base
    estadísticas = {
        'total_productos': Producto.objects.filter(**filtro_fecha).count(),
        'total_categorias': Categoria.objects.count(),
        'total_usuarios': Perfil.objects.filter(**filtro_fecha_usuario).count(),
        'total_resenas': Reseña.objects.filter(**filtro_fecha).count(),
        'filtro_actual': dias,
    }
    
    # 1. Ticket Promedio (AOV)
    # Usar términos en inglés para coincidir con el CHECK constraint de la DB
    pedidos_exitosos = Pedido.objects.filter(estado__in=['delivered', 'shipped', 'Entregado', 'Enviado'])
    avg_order = pedidos_exitosos.aggregate(promedio=Avg('monto_total'))['promedio'] or 0
    estadísticas['ticket_promedio'] = avg_order

    # 2. Datos para el Gráfico (Últimos 6 meses)
    # Buscamos ingresos del histórico real agrupados por mes
    seis_meses_atras = timezone.now() - datetime.timedelta(days=180)
    ventas_mensuales = pedidos_exitosos.filter(creado_el__gte=seis_meses_atras) \
        .annotate(mes=TruncMonth('creado_el')) \
        .values('mes') \
        .annotate(total=Sum('monto_total')) \
        .order_by('mes')

    meses_nombres = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
        7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }

    chart_labels = []
    chart_data = []
    
    for v in ventas_mensuales:
        chart_labels.append(meses_nombres[v['mes'].month])
        # Convertimos a millones o lo dejamos en valor normal (ajustado para visualización)
        # Dividimos por 1M para que el gráfico no tenga etiquetas gigantes
        chart_data.append(float(v['total']) / 1_000_000)

    # Si no hay datos, ponemos datos vacíos para evitar error en JS
    if not chart_labels:
        chart_labels = ['Sin Datos']
        chart_data = [0]

    pedidos = Pedido.objects.filter(**filtro_fecha).select_related('usuario').order_by('-creado_el')
    
    return render(petición, 'admin_panel/reports.html', {
        'estadisticas': estadísticas,
        'pedidos': pedidos,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'titulo_pagina': 'Reportes y Estadísticas — MIKITECH',
    })


@requerir_administrador
def gestion_logistica(petición):
    """Módulo de despacho y entrega de pedidos."""
    estado_filtro = petición.GET.get('estado', 'all')
    
    if estado_filtro != 'all':
        pedidos = Pedido.objects.filter(estado=estado_filtro).select_related('usuario').order_by('-creado_el')
    else:
        pedidos = Pedido.objects.all().select_related('usuario').order_by('-creado_el')

    # Estadísticas rápidas para la vista (Usando términos en inglés de la DB)
    stats = {
        'pendientes': Pedido.objects.filter(estado__in=['pending', 'processing']).count(),
        'en_camino': Pedido.objects.filter(estado='shipped').count(),
        'entregados': Pedido.objects.filter(estado='delivered').count(),
        'filtro_actual': estado_filtro,
    }

    return render(petición, 'admin_panel/logistics.html', {
        'pedidos': pedidos,
        'stats': stats,
        'titulo_pagina': 'Logística y Despacho — MIKITECH',
    })


@requerir_administrador
@require_POST
def cambiar_estado_pedido(petición, id_pedido):
    """Actualiza el estado de un pedido y notifica al cliente si es necesario."""
    pedido = get_object_or_404(Pedido, id=id_pedido)
    if petición.method == 'POST':
        nuevo_estado_es = petición.POST.get('nuevo_estado')
        
        # Mapeo de español (UI) a inglés (DB) para cumplir con el CHECK constraint
        mapping = {
            'Pendiente': 'pending',
            'Enviado': 'shipped',
            'Entregado': 'delivered',
            'Cancelado': 'cancelled'
        }
        
        status_to_save = mapping.get(nuevo_estado_es)
        
        if status_to_save:
            estado_anterior = pedido.estado
            pedido.estado = status_to_save
            pedido.save()
            
            # Notificar al cliente si pasó a 'Entregado'
            if status_to_save == 'delivered' and estado_anterior != 'delivered':
                from interactions.models import Notificacion
                Notificacion.objects.create(
                    id=uuid.uuid4(),
                    usuario=pedido.usuario,
                    mensaje=f"[Pedido Entregado] Tu pedido #{str(pedido.id)[:8]} ha sido entregado exitosamente. Gracias por confiar en MIKITECH!",
                )
                messages.success(petición, f"Pedido #{str(pedido.id)[:8]} marcado como ENTREGADO. Cliente notificado.")
            else:
                messages.success(petición, f"Estado del pedido #{str(pedido.id)[:8]} actualizado a {nuevo_estado_es}.")
            
    return redirect('admin_logistics')


@requerir_administrador
def ver_factura_pedido(petición, id_pedido):
    """Vista detallada de factura para impresión administrativa."""
    pedido = get_object_or_404(Pedido.objects.prefetch_related('detalles__producto'), id=id_pedido)
    perfil = pedido.usuario
    
    # Cálculos de impuestos para la factura legal
    import decimal
    iva_porcentaje = decimal.Decimal('0.19')
    subtotal = pedido.monto_total / (decimal.Decimal('1') + iva_porcentaje)
    iva_monto = pedido.monto_total - subtotal

    return render(petición, 'admin_panel/invoice.html', {
        'pedido': pedido,
        'detalles': pedido.detalles.all(),
        'perfil': perfil,
        'subtotal': subtotal,
        'iva_monto': iva_monto,
        'titulo_pagina': f'Factura #{str(pedido.id)[:8].upper()} — MIKITECH',
    })
