from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden, JsonResponse

def requerir_usuario_autenticado(función_vista):
    """
    Decorador de seguridad para proteger vistas del área privada del cliente.
    Verifica que exista un usuario_id en sesión. Si no existe,
    redirige al formulario de inicio de sesión público preservando la URL original en 'next'.
    """
    @wraps(función_vista)
    def envoltura(petición, *args, **kwargs):
        if not petición.session.get('usuario_id'):
            return redirect(f'/cuenta/ingreso/?next={petición.path}')
        return función_vista(petición, *args, **kwargs)
    return envoltura


def requiere_permiso(codigo_permiso):
    """
    Decorador para restringir el acceso a vistas según permisos de RBAC.
    """
    def decorador(funcion_vista):
        @wraps(funcion_vista)
        def envoltura(request, *args, **kwargs):
            # 1. Verificar si el usuario está autenticado
            usuario_id = request.session.get('usuario_id')
            token = None
            
            # Comprobar cabecera Authorization (JWT)
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
                from django.conf import settings
                if token == 'mock-local-token' and getattr(settings, 'USE_SQLITE', False):
                    usuario_id = request.session.get('usuario_id') or 'mock-local-user-id'
                else:
                    from users.supabase_auth import verificar_token_supabase
                    datos_user, error = verificar_token_supabase(token)
                    if datos_user:
                        usuario_id = datos_user.get('id')

            if not usuario_id:
                if request.headers.get('Accept') == 'application/json' or request.path.startswith('/api/'):
                    return JsonResponse({'error': 'No autenticado'}, status=401)
                return redirect(f'/cuenta/ingreso/?next={request.path}')

            # 2. Obtener los permisos del usuario
            permisos = getattr(request, 'permisos_usuario', None)
            if permisos is None:
                # Fallback: cargar los permisos de la base de datos si el middleware no lo hizo
                from users.models import Perfil
                try:
                    perfil = Perfil.objects.select_related('rol_rbac').prefetch_related('rol_rbac__permisos').get(id=usuario_id)
                    request.perfil_usuario = perfil
                    request.permisos_usuario = list(perfil.rol_rbac.permisos.values_list('codigo', flat=True)) if perfil.rol_rbac else []
                    permisos = request.permisos_usuario
                except Exception:
                    permisos = []

            # 3. Validar si el usuario posee el permiso requerido
            if codigo_permiso not in permisos:
                if request.headers.get('Accept') == 'application/json' or request.path.startswith('/api/'):
                    return JsonResponse({'error': 'Forbidden: No tienes el permiso requerido'}, status=403)
                return HttpResponseForbidden("<h1>403 Forbidden</h1><p>No tienes permiso para acceder a esta página.</p>")

            return funcion_vista(request, *args, **kwargs)
        return envoltura
    return decorador
