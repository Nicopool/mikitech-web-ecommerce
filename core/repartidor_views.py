from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from interactions.models import Pedido
from django.conf import settings

from functools import wraps

# Para simplificar y dado que el rol se maneja en base de datos vía Supabase,
# estableceremos un gateway similar al de admin, pero enfocado en logísticas.
CODIGO_REPARTIDOR = getattr(settings, 'DELIVERY_GATEWAY_CODE', 'MOTO-2026')

def requiere_repartidor(función_vista):
    """
    Decorador de triple cerrojo para rutas de repartidores (ISO 25010 – Seguridad).

    Verifica en orden:
    1. Que exista una sesión activa con usuario_id.
    2. Que el rol de sesión sea 'repartidor' (sincronizado con BD por RoleVerificationMiddleware).
    3. Que se haya superado la pasarela logística MOTO-2026 en la sesión actual,
       impidiendo acceso directo sin pasar por la pasarela de seguridad.
    """
    @wraps(función_vista)
    def envoltura(petición, *args, **kwargs):
        # Cerrojo 1: debe haber sesión activa
        if not petición.session.get('usuario_id'):
            return redirect('/repartidor/pasarela/')

        # Cerrojo 2: el rol de sesión (sincronizado con BD) debe ser 'repartidor'
        if petición.session.get('rol_usuario') != 'repartidor':
            return redirect('/repartidor/pasarela/')

        # Cerrojo 3: debe haber superado la pasarela de código MOTO-2026
        if not petición.session.get('pasarela_repartidor_superada'):
            return redirect('/repartidor/pasarela/')

        return función_vista(petición, *args, **kwargs)
    return envoltura


def pasarela_repartidor(petición):
    """Pasarela de seguridad inicial solicitando código para repartidores."""
    # 1. Si no hay sesión activa (usuario no autenticado), denegar acceso de inmediato
    if not petición.session.get('usuario_id'):
        return redirect('/cuenta/ingreso/?next=/repartidor/pasarela/')

    rol = petición.session.get('rol_usuario')
    if rol == 'repartidor':
        return redirect('/repartidor/')

    if petición.session.get('pasarela_repartidor_superada'):
        return redirect('/repartidor/login/')

    if petición.method == 'POST':
        codigo_enviado = petición.POST.get('codigo_secreto', '').strip()
        if codigo_enviado == CODIGO_REPARTIDOR:
            petición.session['pasarela_repartidor_superada'] = True
            petición.session.modified = True
            return redirect('/repartidor/login/')
        return render(petición, 'core/gateway_repartidor.html', {
            'error': 'Código de acceso incorrecto.',
            'titulo_pagina': 'Acceso Repartidores — MIKITECH'
        })

    return render(petición, 'core/gateway_repartidor.html', {
        'titulo_pagina': 'Acceso Repartidores — MIKITECH'
    })


def login_repartidor(petición):
    """Acceso exclusivo e independiente para personal de despachos."""
    if not petición.session.get('pasarela_repartidor_superada'):
        return redirect('/repartidor/pasarela/')
        
    if petición.session.get('rol_usuario') == 'repartidor':
        return redirect('/repartidor/')
        
    if petición.method == 'POST':
        from users.supabase_auth import iniciar_sesion_usuario
        correo = petición.POST.get('correo', '').strip()
        clave = petición.POST.get('clave', '')
        
        datos, error = iniciar_sesion_usuario(correo, clave)
        
        if error:
            return render(petición, 'core/repartidor_login.html', {
                'error': 'Credenciales logísticas incorrectas.',
                'correo': correo,
            })
            
        id_usuario = datos.get('user', {}).get('id')
        from users.models import Perfil
        try:
            perfil = Perfil.objects.get(id=id_usuario)
            if perfil.rol != 'repartidor':
                return render(petición, 'core/repartidor_login.html', {
                    'error': 'Tu cuenta NO pertenece al escuadrón motorizado.',
                })
            petición.session['usuario_id'] = id_usuario
            petición.session['token_acceso'] = datos.get('access_token')
            petición.session['rol_usuario'] = 'repartidor'
            petición.session['pasarela_repartidor_superada'] = True  # Confirmar autorización completa
            petición.session['nombre_usuario'] = perfil.nombre_usuario
            petición.session.modified = True
            return redirect('/repartidor/')
        except Perfil.DoesNotExist:
            return render(petición, 'core/repartidor_login.html', {
                'error': 'Perfil no sincroznizado en matriz logística.',
            })

    return render(petición, 'core/repartidor_login.html', {
        'titulo_pagina': 'Acceso Escuadra - MIKITECH'
    })


def registro_repartidor(petición):
    """Creación independiente de perfiles de repartición."""
    if not petición.session.get('pasarela_repartidor_superada'):
        return redirect('/repartidor/pasarela/')
        
    if petición.session.get('rol_usuario') == 'repartidor':
        return redirect('/repartidor/')

    if petición.method == 'POST':
        from users.supabase_auth import registrar_usuario_sql
        from users.models import Perfil
        nombre_completo = petición.POST.get('nombre_completo', '').strip()
        nombre_usuario = petición.POST.get('nombre_usuario', '').strip()
        correo = petición.POST.get('correo', '').strip()
        clave = petición.POST.get('clave', '')
        
        ctx = {
            'nombre_completo': nombre_completo,
            'nombre_usuario': nombre_usuario,
            'correo': correo,
        }
        
        if not all([nombre_completo, nombre_usuario, correo, clave]):
            ctx['error'] = 'Completa todo el sumario operativo.'
            return render(petición, 'core/repartidor_register.html', ctx)
            
        datos, error = registrar_usuario_sql(correo, clave, nombre_completo, nombre_usuario, 'repartidor')
        
        if error:
            ctx['error'] = error
            return render(petición, 'core/repartidor_register.html', ctx)
            
        # Bypass email confirmation
        try:
            from django.db import connection
            table_name = '"auth.users"' if connection.vendor == 'sqlite' else "auth.users"
            now_func = "datetime('now')" if connection.vendor == 'sqlite' else "NOW()"
            with connection.cursor() as cursor:
                cursor.execute(
                    f"UPDATE {table_name} SET email_confirmed_at = {now_func} WHERE email = %s", 
                    [correo]
                )
        except Exception:
            pass

        return render(petición, 'core/repartidor_login.html', {
            'success': 'Has sido reclutado logísticamente. Identifícate para entrar en servicio.'
        })

    return render(petición, 'core/repartidor_register.html', {
        'titulo_pagina': 'Reclutamiento - MIKITECH'
    })


def cerrar_sesion_repartidor(petición):
    petición.session.flush()
    return redirect('/repartidor/pasarela/')


@requiere_repartidor
def panel_repartidor(petición):
    """Panel principal donde los repartidores ven los pedidos para entregar."""
    from users.models import Perfil
    # Obtener al repartidor actual
    repartidor_actual = get_object_or_404(Perfil, id=petición.session.get('usuario_id'))

    # Pedidos pendientes sin asignar, y pedidos asignados a este repartidor
    pedidos_sin_asignar = Pedido.objects.filter(estado__in=['processing', 'shipped'], repartidor__isnull=True).order_by('-creado_el')
    mis_pedidos = Pedido.objects.filter(estado__in=['processing', 'shipped'], repartidor=repartidor_actual).order_by('-creado_el')
    
    return render(petición, 'core/repartidor_panel.html', {
        'pedidos_sin_asignar': pedidos_sin_asignar,
        'mis_pedidos': mis_pedidos,
        'repartidor_actual': repartidor_actual,
        'titulo_pagina': 'Panel de Repartidor — MIKITECH'
    })


@requiere_repartidor
def asignar_pedido(petición, id_pedido):
    """Permite a un repartidor reclamar un pedido."""
    pedido = get_object_or_404(Pedido, id=id_pedido)
    from users.models import Perfil
    repartidor_actual = get_object_or_404(Perfil, id=petición.session.get('usuario_id'))

    if not pedido.repartidor:
        pedido.repartidor = repartidor_actual
        pedido.save()
        messages.success(petición, f"¡Te has asignado el pedido {pedido.id} exitosamente!")
    else:
        messages.error(petición, "Ups... Este pedido ya ha sido reclamado por otro piloto.")
        
    return redirect('core:repartidor')


@requiere_repartidor
def entregar_pedido(petición, id_pedido):
    """Procesa la entrega de un pedido validando la cédula del cliente."""
    pedido = get_object_or_404(Pedido, id=id_pedido)
    
    if petición.method == 'POST':
        cedula_ingresada = petición.POST.get('cedula_cliente', '').strip()
        notas = petición.POST.get('notas', '').strip()
        
        # Validar la cédula
        if cedula_ingresada == pedido.cedula:
            pedido.estado = 'delivered'
            pedido.entregado_el = timezone.now()
            pedido.notas_repartidor = notas
            pedido.save()
            messages.success(petición, f"Entregado exitosamente. Pedido: {pedido.id}")
            return redirect('core:repartidor')
        else:
            return render(petición, 'core/repartidor_panel.html', {
                'pedidos': Pedido.objects.filter(estado__in=['processing', 'shipped']).order_by('-creado_el'),
                'error_modal': f"La cédula no coincide para el pedido {pedido.id}.",
                'pedido_error_id': str(pedido.id),
                'titulo_pagina': 'Panel de Repartidor — MIKITECH'
            })
    
    return redirect('core:repartidor')
