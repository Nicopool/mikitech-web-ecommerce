"""Vistas de la aplicación usuarios — ingreso, registro y área privada — MIKITECH"""

import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from .supabase_auth import iniciar_sesion_usuario, registrar_usuario
from .models import Perfil
from interactions.models import Favorito


def vista_ingreso(petición):
    """Iniciar sesión con Supabase Auth."""
    if petición.session.get('usuario_id'):
        return redirect('users:profile')

    if petición.method == 'POST':
        correo    = petición.POST.get('correo', '').strip()
        clave     = petición.POST.get('clave', '')
        recordar  = petición.POST.get('recordarme')  # CP-MK-015: Recordarme

        # CP-MK-011: Campos vacíos bloqueados desde backend
        if not correo or not clave:
            return render(petición, 'users/login.html', {
                'error': 'Por favor completa todos los campos.',
                'next': petición.POST.get('next', '')
            })

        # Validación estricta de formato de email (prevención SQLi básico)
        import re
        if not re.match(r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', correo):
            return render(petición, 'users/login.html', {
                'error': 'Formato de correo inválido.',
                'correo': correo,
                'next': petición.POST.get('next', '')
            })

        datos, error = iniciar_sesion_usuario(correo, clave)

        if error:
            # Clasificar el error de Supabase para mostrar alertas espíficas
            error_lower = str(error).lower()

            if 'invalid login credentials' in error_lower or 'invalid email or password' in error_lower:
                # Correo o contraseña incorrectos
                mensaje_error = 'El correo electrónico o la contraseña son incorrectos. Verifica tus datos e intenta de nuevo.'
                tipo_error = 'credenciales'

            elif 'email not confirmed' in error_lower or 'email link is invalid' in error_lower:
                # Correo no verificado en Supabase
                mensaje_error = 'Tu correo aún no ha sido verificado. Revisa tu bandeja de entrada y haz clic en el enlace de confirmación.'
                tipo_error = 'no_confirmado'

            elif 'user not found' in error_lower or 'no user found' in error_lower:
                # Correo no registrado
                mensaje_error = 'No existe ninguna cuenta con ese correo electrónico. ¿Quieres <a href="/cuenta/registro/">crear una cuenta</a>?'
                tipo_error = 'no_encontrado'

            elif 'google' in error_lower or 'oauth' in error_lower or 'provider' in error_lower or 'social' in error_lower:
                # Cuenta creada con Google (OAuth), no tiene contraseña de email
                mensaje_error = 'Esta cuenta fue creada con Google. Usa el botón “Iniciar sesión con Google” o recupera tu contraseña.'
                tipo_error = 'google'

            elif 'rate limit' in error_lower or 'too many' in error_lower:
                # Límite de intentos excedido
                mensaje_error = 'Demasiados intentos fallidos. Espera unos minutos antes de intentarlo de nuevo.'
                tipo_error = 'rate_limit'

            elif 'network' in error_lower or 'connection' in error_lower or 'timeout' in error_lower or 'urlopen error' in error_lower:
                # Error de red / Supabase caído
                mensaje_error = 'No se pudo conectar con el servidor de autenticación. Verifica tu conexión a internet e intenta de nuevo.'
                tipo_error = 'red'

            else:
                # Error genérico desconocido
                mensaje_error = 'Ocurrió un error al iniciar sesión. Intenta de nuevo o contacta con soporte.'
                tipo_error = 'desconocido'

            return render(petición, 'users/login.html', {
                'error': mensaje_error,
                'error_tipo': tipo_error,
                'correo': correo,
                'next': petición.POST.get('next', '')
            })

        # CP-MK-015: Persistencia de sesión según checkbox "Recordarme"
        # Si marcó "Recordarme" → sesión persiste 30 días (2 592 000 s)
        # Si no → sesión expira al cerrar el navegador (set_expiry(0))
        if recordar:
            petición.session.set_expiry(2592000)  # 30 días
        else:
            petición.session.set_expiry(0)         # Solo navegador abierto

        # Guardar sesión
        id_usuario = datos.get('user', {}).get('id')
        petición.session['usuario_id']    = id_usuario
        petición.session['token_acceso']  = datos.get('access_token')

        # Obtener o crear perfil
        perfil = None
        try:
            perfil = Perfil.objects.get(id=id_usuario)
            petición.session['rol_usuario']    = perfil.rol
            petición.session['nombre_usuario'] = perfil.nombre_usuario
            petición.session['avatar_url']     = perfil.url_avatar or ''
        except Perfil.DoesNotExist:
            petición.session['rol_usuario'] = 'client'
            petición.session['avatar_url']  = ''

        proxima_url = petición.GET.get('next', '/cuenta/perfil/')
        nombre = perfil.nombre_mostrado if perfil else 'Usuario'
        messages.success(petición, f'✅ ¡Login exitoso! Bienvenido de vuelta a tu panel, {nombre}.')
        return redirect(proxima_url)

    return render(petición, 'users/login.html', {
        'titulo_pagina': 'Iniciar Sesión — MIKITECH',
        'next': petición.GET.get('next', '')
    })


def vista_registro(petición):
    """Registrar nuevo usuario mediante el formulario público."""
    if petición.session.get('usuario_id'):
        return redirect('users:profile')

    if petición.method == 'POST':
        import html
        nombre_completo = html.escape(petición.POST.get('nombre_completo', '').strip())
        nombre_usuario = html.escape(petición.POST.get('nombre_usuario', '').strip())
        correo = petición.POST.get('correo', '').strip()
        clave = petición.POST.get('clave', '')
        clave2 = petición.POST.get('clave2', '')
        terminos = petición.POST.get('terminos')

        contexto = {
            'nombre_completo': nombre_completo,
            'nombre_usuario': nombre_usuario,
            'correo': correo,
            'titulo_pagina': 'Crear Cuenta — MIKITECH',
        }

        if not terminos:
            contexto['error'] = 'Debes aceptar los Términos y Condiciones.'
            return render(petición, 'users/register.html', contexto)

        if not all([nombre_completo, nombre_usuario, correo, clave]):
            contexto['error'] = 'Por favor completa todos los campos del formulario.'
            return render(petición, 'users/register.html', contexto)

        import re
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
            contexto['error'] = 'Formato de correo inválido.'
            return render(petición, 'users/register.html', contexto)

        # Solo se permiten correos de Gmail o Hotmail/Outlook
        DOMINIOS_PERMITIDOS = {
            'gmail.com', 'hotmail.com', 'hotmail.es',
            'outlook.com', 'outlook.es', 'live.com', 'live.com.mx'
        }
        dominio_correo = correo.split('@')[-1].lower() if '@' in correo else ''
        if dominio_correo not in DOMINIOS_PERMITIDOS:
            contexto['error'] = 'Solo se aceptan correos de Gmail (@gmail.com) o Hotmail/Outlook (@hotmail.com, @outlook.com).'
            return render(petición, 'users/register.html', contexto)

        if clave != clave2:
            contexto['error'] = 'Las contraseñas no coinciden.'
            return render(petición, 'users/register.html', contexto)

        patron = r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$"
        if not re.match(patron, clave):
            contexto['error'] = 'La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial (@$!%*?&).'
            return render(petición, 'users/register.html', contexto)

        if Perfil.objects.filter(nombre_usuario=nombre_usuario).exists():
            contexto['error'] = 'Ese nombre de usuario ya está registrado.'
            return render(petición, 'users/register.html', contexto)

        # Verificar si el correo electrónico ya existe en auth.users
        from django.db import connection
        from django.conf import settings
        table_name = '"auth.users"' if getattr(settings, 'USE_SQLITE', False) else 'auth.users'
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT id FROM {table_name} WHERE email = %s", [correo])
                if cursor.fetchone():
                    contexto['error'] = 'Este correo electrónico ya está registrado. Intenta iniciar sesión.'
                    return render(petición, 'users/register.html', contexto)
        except Exception as e:
            print(f"[vista_registro] Error verificando duplicidad de correo: {e}")

        from .supabase_auth import registrar_usuario, registrar_usuario_sql
        datos, error = registrar_usuario(correo, clave, nombre_completo, nombre_usuario)

        # Si el error es específicamente por el envío de correo de confirmación de Supabase,
        # intentamos registrar al usuario directamente en la base de datos (fallback de emergencia).
        if error and "confirmation email" in error.lower():
            print("[!] Supabase SMTP falló. Iniciando registro directo vía SQL...")
            datos, error = registrar_usuario_sql(correo, clave, nombre_completo, nombre_usuario)

        if error:
            contexto['error'] = f'Error en el registro: {error}'
            return render(petición, 'users/register.html', contexto)

        # Supabase devuelve un response exitoso con identities=[] cuando el email ya existe,
        # en vez de devolver un error explícito. Detectamos este caso.
        user_data = datos.get('user', {}) if datos else {}
        id_usuario = user_data.get('id')
        identities = user_data.get('identities', None)

        if not id_usuario or (isinstance(identities, list) and len(identities) == 0):
            contexto['error'] = 'Este correo electrónico ya está registrado. Intenta iniciar sesión.'
            return render(petición, 'users/register.html', contexto)
        
        # Sincronizar el perfil local inmediatamente.
        # Usamos update_or_create porque un trigger en Supabase puede haber creado ya el registro.
        Perfil.objects.update_or_create(
            id=id_usuario,
            defaults={
                'nombre_completo': nombre_completo,
                'nombre_usuario': nombre_usuario,
                'rol': 'client'
            }
        )

        return render(petición, 'users/login.html', {
            'success': '✅ ¡Tu registro ha sido exitoso! Ya puedes iniciar sesión con tus credenciales.',
            'titulo_pagina': 'Iniciar Sesión — MIKITECH'
        })

    return render(petición, 'users/register.html', {'titulo_pagina': 'Crear Cuenta — MIKITECH'})


def vista_cerrar_sesion(petición):
    """Limpia la sesión de Django y redirige al inicio."""
    petición.session.flush()
    messages.info(petición, 'Has cerrado tu sesión correctamente. ¡Vuelve pronto!')
    return redirect('core:home')


def mi_perfil(petición):
    """Área privada: Tablero principal del perfil del usuario."""
    if not petición.session.get('usuario_id'):
        return redirect(f'/cuenta/login/?next=/cuenta/perfil/')

    try:
        perfil = Perfil.objects.get(id=petición.session['usuario_id'])
    except Perfil.DoesNotExist:
        petición.session.flush()
        return redirect('users:login')

    from interactions.models import Reseña
    from django.db import connection
    
    conteo_resenas = Reseña.objects.filter(usuario=perfil).count()
    
    # Consulta directa para pedidos en Supabase
    from interactions.models import Pedido
    pedidos_qs = Pedido.objects.filter(usuario=perfil).order_by('-creado_el')
    conteo_pedidos = pedidos_qs.count()
    pedidos_recientes = pedidos_qs[:3]

    # Datos para Chart.js (ordenados cronológicamente)
    pedidos_cronologicos = list(pedidos_qs)[::-1]
    fechas_chart = [p.creado_el.strftime("%d/%m") for p in pedidos_cronologicos]
    montos_chart = [float(p.monto_total) for p in pedidos_cronologicos]

    reseñas_recientes = Reseña.objects.filter(usuario=perfil).select_related('producto').order_by('-creado_el')[:3]
    
    from interactions.models import Favorito
    favoritos_recientes = Favorito.objects.filter(usuario=perfil).select_related('producto').order_by('-creado_el')[:4]

    pedidos_entregados = sum(1 for p in pedidos_qs if getattr(p, 'estado', '') in ['delivered', 'Entregado', 'Completado'])

    return render(petición, 'users/profile.html', {
        'perfil': perfil,
        'titulo_pagina': f'Mi Panel — {perfil.nombre_mostrado} | MIKITECH',
        'conteo_resenas': conteo_resenas,
        'conteo_pedidos': conteo_pedidos,
        'pedidos_entregados': pedidos_entregados,
        'resenas_recientes': reseñas_recientes,
        'pedidos_recientes': pedidos_recientes,
        'favoritos_recientes': favoritos_recientes,
        'fechas_chart': fechas_chart,
        'montos_chart': montos_chart,
    })


def editar_perfil(petición):
    """Formulario para actualizar los datos personales y avatar."""
    if not petición.session.get('usuario_id'):
        return redirect(f'/cuenta/login/?next=/cuenta/perfil/editar/')

    try:
        perfil = Perfil.objects.get(id=petición.session['usuario_id'])
    except Perfil.DoesNotExist:
        return redirect('users:login')

    if petición.method == 'POST':
        import html

        # Actualizar campos de texto solo si están presentes en la petición POST
        # Esto evita errores de None y permite peticiones parciales (como subir solo el avatar)
        if 'nombre_completo' in petición.POST:
            val = petición.POST.get('nombre_completo')
            perfil.nombre_completo = html.escape(val.strip()) if val else ''
        if 'biografia' in petición.POST:
            val = petición.POST.get('biografia')
            perfil.biografia = html.escape(val.strip()) if val else ''
        if 'telefono' in petición.POST:
            val = petición.POST.get('telefono')
            perfil.telefono = html.escape(val.strip()) if val else ''
        if 'ciudad' in petición.POST:
            val = petición.POST.get('ciudad')
            perfil.ciudad = html.escape(val.strip()) if val else ''
        if 'pais' in petición.POST:
            val = petición.POST.get('pais')
            perfil.pais = html.escape(val.strip()) if val else 'Colombia'

        # Manejo del Avatar
        if 'avatar' in petición.FILES:
            import os
            from django.core.files.storage import default_storage
            from .supabase_auth import subir_a_supabase_storage
            archivo_avatar = petición.FILES['avatar']
            extension = os.path.splitext(archivo_avatar.name)[1].lower()
            if extension in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                nombre_archivo = f"avatars/{perfil.id}{extension}"
                try:
                    datos_archivo = archivo_avatar.read()
                    archivo_avatar.seek(0)  # Reset pointer in case fallback needs it
                    public_url, error_storage = subir_a_supabase_storage(nombre_archivo, datos_archivo, archivo_avatar.content_type)
                    if public_url:
                        perfil.url_avatar = public_url
                    else:
                        print(f"[!] Fallback a local. Error de storage: {error_storage}")
                        nombre_guardado = default_storage.save(nombre_archivo, archivo_avatar)
                        perfil.url_avatar = f'/media/{nombre_guardado}'
                except Exception as ex:
                    print(f"[!] Fallback a local. Excepción: {ex}")
                    nombre_guardado = default_storage.save(nombre_archivo, archivo_avatar)
                    perfil.url_avatar = f'/media/{nombre_guardado}'

        perfil.save()

        # Sincronizar los datos en la sesión de Django para que se reflejen en toda la app inmediatamente
        petición.session['avatar_url'] = perfil.url_avatar or ''
        petición.session['nombre_usuario'] = perfil.nombre_usuario
        petición.session.modified = True
        
        # Respuesta JSON para peticiones AJAX (fetch)
        if petición.headers.get('x-requested-with') == 'XMLHttpRequest' or petición.content_type == 'application/json':
            from django.http import JsonResponse
            return JsonResponse({
                'success': True, 
                'message': 'Perfil actualizado correctamente',
                'avatar_url': perfil.url_avatar or ''
            })
            
        messages.success(petición, "Perfil actualizado correctamente.")
        return redirect('users:profile')

    return render(petición, 'users/edit_profile.html', {
        'perfil': perfil,
        'titulo_pagina': 'Editar Perfil — MIKITECH',
    })


def mis_favoritos(petición):
    """Lista de productos marcados como favoritos por el usuario."""
    if not petición.session.get('usuario_id'):
        return redirect(f'/cuenta/login/?next=/cuenta/favoritos/')

    try:
        perfil = Perfil.objects.get(id=petición.session['usuario_id'])
        favoritos = Favorito.objects.filter(usuario=perfil).select_related('producto').order_by('-creado_el')
    except Perfil.DoesNotExist:
        favoritos = []

    return render(petición, 'users/favorites.html', {
        'perfil': perfil,
        'favoritos': favoritos,
        'titulo_pagina': 'Mis Favoritos — MIKITECH',
    })


def mis_pedidos(petición):
    """Historial de transacciones y estados de envío."""
    if not petición.session.get('usuario_id'):
        return redirect(f'/cuenta/login/?next=/cuenta/pedidos/')

    try:
        from users.models import Perfil
        perfil = Perfil.objects.get(id=petición.session['usuario_id'])
        from interactions.models import Pedido
        pedidos = Pedido.objects.filter(usuario=perfil).select_related('repartidor').order_by('-creado_el')
    except Exception as e:
        print("Error obteniendo pedidos:", e)
        pedidos = []

    pedidos_entregados = sum(1 for p in pedidos if p.estado == 'delivered')
    pedidos_en_transito = sum(1 for p in pedidos if p.estado in ['pending', 'processing', 'shipped'])

    return render(petición, 'users/orders.html', {
        'perfil': perfil,
        'orders': pedidos,
        'orders_delivered': pedidos_entregados,
        'orders_transit': pedidos_en_transito,
        'page_title': 'Mis Pedidos — MIKITECH',
    })


def olvide_contraseña(petición):
    """Página para iniciar la recuperación de cuenta."""
    if petición.method == 'POST':
        correo = petición.POST.get('correo', '').strip()
        if not correo:
            return render(petición, 'users/forgot_password.html', {'error': 'Ingresa tu correo.', 'titulo_pagina': 'Recuperar Contraseña'})

        from .supabase_auth import enviar_recuperacion_contraseña
        datos, error = enviar_recuperacion_contraseña(correo)

        if error:
            # Supabase retorna éxito incluso si el email no existe (por seguridad)
            # Solo mostramos error en fallos de red reales
            pass

        # Siempre redirigir al formulario de código (por seguridad no revelamos si el email existe)
        petición.session['correo_recuperacion'] = correo
        messages.success(petición, f'¡Listo! Si {correo} está registrado, recibirás un enlace en tu correo. Abre el enlace, copia el código largo que aparece y pégalo aquí. Revisa también spam.')
        return redirect('users:reset_password')

    return render(petición, 'users/forgot_password.html', {'titulo_pagina': 'Recuperar Contraseña'})


def restablecer_contraseña(petición):
    """Verifica el código OTP y actualiza la contraseña del usuario."""
    correo = petición.session.get('correo_recuperacion', '')

    if petición.method == 'GET' and not correo:
        return redirect('users:forgot_password')

    if petición.method == 'POST':
        correo_post = petición.POST.get('correo', '').strip()
        correo = correo or correo_post

        token = petición.POST.get('token', '').strip()
        clave = petición.POST.get('clave', '')
        confirmar_clave = petición.POST.get('confirmar_clave', '')

        contexto = {'email': correo, 'titulo_pagina': 'Ingresar Código'}

        if not correo or not token or not clave:
            contexto['error'] = 'Completa todos los campos.'
            return render(petición, 'users/reset_password.html', contexto)

        if clave != confirmar_clave:
            contexto['error'] = 'Las contraseñas no coinciden.'
            return render(petición, 'users/reset_password.html', contexto)

        import re
        patron = r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$"
        if not re.match(patron, clave):
            contexto['error'] = 'La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial.'
            return render(petición, 'users/reset_password.html', contexto)

        from .supabase_auth import verificar_otp_recuperacion
        datos, error = verificar_otp_recuperacion(correo, token, clave)

        if error:
            contexto['error'] = 'Código inválido o expirado. Solicita uno nuevo.'
            return render(petición, 'users/reset_password.html', contexto)

        if 'correo_recuperacion' in petición.session:
            del petición.session['correo_recuperacion']

        messages.success(petición, '¡Contraseña actualizada correctamente! Ya puedes ingresar.')
        return redirect('users:login')

    return render(petición, 'users/reset_password.html', {'email': correo, 'titulo_pagina': 'Ingresar Código'})


def mi_historial(petición):
    """Resumen de toda la actividad del usuario en la plataforma."""
    if not petición.session.get('usuario_id'):
        return redirect('users:login')

    try:
        perfil = Perfil.objects.get(id=petición.session['usuario_id'])
    except Perfil.DoesNotExist:
        return redirect('users:login')

    from interactions.models import Favorito, Voto, Reseña, Pedido
    reseñas = Reseña.objects.filter(usuario=perfil).select_related('producto').order_by('-creado_el')
    votos = Voto.objects.filter(usuario=perfil).select_related('producto').order_by('-creado_el')
    favoritos = Favorito.objects.filter(usuario=perfil).select_related('producto').order_by('-creado_el')
    pedidos = Pedido.objects.filter(usuario=perfil).order_by('-creado_el')

    return render(petición, 'users/history.html', {
        'perfil': perfil,
        'titulo_pagina': 'Mi Historial — MIKITECH',
        'resenas': reseñas,
        'votos': votos,
        'favoritos': favoritos,
        'pedidos': pedidos,
        'conteo_resenas': reseñas.count(),
        'conteo_votos': votos.count(),
        'conteo_favoritos': favoritos.count(),
        'conteo_pedidos': pedidos.count(),
    })


def mis_reportes(petición):
    """Acceso a archivos PDF y estadísticas descargables."""
    if not petición.session.get('usuario_id'):
        return redirect('users:login')

    try:
        perfil = Perfil.objects.get(id=petición.session['usuario_id'])
    except Perfil.DoesNotExist:
        return redirect('users:login')

    from interactions.models import Voto, Reseña, Pedido
    from django.db import connection

    conteo_resenas = Reseña.objects.filter(usuario=perfil).count()
    conteo_votos = Voto.objects.filter(usuario=perfil).count()
    reseñas = Reseña.objects.filter(usuario=perfil).select_related('producto')
    
    # Usar ORM con prefetch para tener los productos listos para la factura PDF
    pedidos = Pedido.objects.filter(usuario=perfil).prefetch_related('detalles__producto').order_by('-creado_el')

    # Pedidos entregados en las últimas 24 horas para lanzar notificaciones toast
    from django.utils import timezone
    from datetime import timedelta
    from django.db.models import Q
    hace_24h = timezone.now() - timedelta(hours=24)
    pedidos_entregados_recientes = pedidos.filter(
        estado='delivered'
    ).filter(
        Q(entregado_el__gte=hace_24h) | Q(entregado_el__isnull=True, actualizado_el__gte=hace_24h)
    )
    
    recientes_list = [
        {
            'id': str(p.id),
            'id_corto': str(p.id)[:8].upper()
        }
        for p in pedidos_entregados_recientes
    ]

    import json

    return render(petición, 'users/reports.html', {
        'perfil': perfil,
        'titulo_pagina': 'Mis Reportes — MIKITECH',
        'conteo_resenas': conteo_resenas,
        'conteo_votos': conteo_votos,
        'resenas': reseñas,
        'orders': pedidos,
        'conteo_pedidos': pedidos.count(),
        'recent_deliveries': json.dumps(recientes_list),
    })


def mark_notifications_read(request):
    """Marcar todas las notificaciones del usuario como leídas."""
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        from users.models import Notificacion
        Notificacion.objects.filter(usuario_id=usuario_id, esta_leida=False).update(esta_leida=True)
    return redirect(request.META.get('HTTP_REFERER', '/'))
