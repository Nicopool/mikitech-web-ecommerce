"""
Middleware de seguridad — MIKITECH

NoCacheMiddleware: Previene que el navegador muestre páginas cacheadas tras cerrar sesión.
RoleVerificationMiddleware: Sincroniza el rol de sesión con la base de datos en cada
                            petición, evitando que una sesión obsoleta conserve privilegios
                            elevados tras una degradación de rol (ISO 25010 – Seguridad).
"""


from django.shortcuts import redirect
from django.contrib import messages

class NoCacheMiddleware:
    """
    Agrega headers Cache-Control a las rutas protegidas (/cuenta/, /admin-panel/)
    para que el navegador no muestre páginas desde caché tras cerrar sesión.
    """

    RUTAS_PROTEGIDAS = ('/cuenta', '/admin-panel', '/repartidor')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Solo aplicar a rutas protegidas que requieren autenticación
        if any(request.path.startswith(ruta) for ruta in self.RUTAS_PROTEGIDAS):
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'

        return response


class RoleVerificationMiddleware:
    """
    ISO 25010 – Control de Acceso Basado en Roles (RBAC) en tiempo real.

    En cada petición a rutas protegidas, consulta la tabla 'profiles' para
    obtener el rol actualizado del usuario y lo escribe en la sesión.

    Esto garantiza que:
    - Si un admin es degradado a 'client' en la base de datos, pierde acceso
      inmediatamente en la siguiente petición, sin necesidad de cerrar sesión.
    - Si un perfil es desactivado (esta_activo=False), la sesión se invalida.
    - El rol que viaja en la sesión siempre es el canon de la base de datos.
    """

    # Rutas que requieren verificación de rol en tiempo real
    RUTAS_VERIFICACION = ('/cuenta', '/admin-panel', '/repartidor')

    # Rutas de acceso público dentro de las rutas verificadas (pasarelas, login, registro)
    RUTAS_EXCLUIDAS = (
        '/cuenta/ingreso/',
        '/cuenta/registro/',
        '/cuenta/recuperar/',
        '/admin-panel/pasarela/',
        '/admin-panel/login/',
        '/admin-panel/registro/',
        '/repartidor/pasarela/',
        '/repartidor/login/',
        '/repartidor/registro/',
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self._verificar_y_sincronizar_rol(request)
        
        # Enforce forced password change for invited admins
        response_pw = self._enforce_forced_password_change(request)
        if response_pw:
            return response_pw
            
        # Enforce strict segregation of duties (RBAC)
        response = self._enforce_strict_panel_isolation(request)
        if response:
            return response
            
        return self.get_response(request)

    def _enforce_forced_password_change(self, request):
        """
        If a user has not changed their temporary password, redirect them immediately
        to the forced password change view for any request under /admin-panel/
        (except logout and the change password page itself).
        """
        perfil = getattr(request, 'perfil_usuario', None)
        if not perfil or perfil.password_cambiada:
            return None

        path = request.path
        if path.startswith('/admin-panel/'):
            # Allow logout and the forced change password page
            if path in ('/admin-panel/logout/', '/admin-panel/cambiar-contrasena/'):
                return None
            
            if path.startswith('/admin-panel/static/') or path.startswith('/admin-panel/media/'):
                return None

            from django.contrib import messages
            try:
                messages.warning(request, 'Debes cambiar tu contraseña temporal antes de poder acceder al panel.')
            except Exception:
                pass
            return redirect('/admin-panel/cambiar-contrasena/')
        
        return None

    def _verificar_y_sincronizar_rol(self, request):
        """Autentica al usuario por token JWT o Sesión, y precarga su Perfil, Rol y Permisos."""
        # Inicializar atributos por defecto en la petición para evitar AttributeError en las vistas
        request.perfil_usuario = None
        request.permisos_usuario = []

        # Solo actuar en rutas protegidas
        if not any(request.path.startswith(ruta) for ruta in self.RUTAS_VERIFICACION):
            return

        # No verificar en rutas de acceso público (login, pasarela, registro)
        if any(request.path.startswith(ruta) for ruta in self.RUTAS_EXCLUIDAS):
            return

        usuario_id = None
        token = None

        # 1. Comprobar cabecera Authorization (JWT)
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

        # 2. Si no hay JWT, recurrir a la sesión tradicional
        if not usuario_id:
            usuario_id = request.session.get('usuario_id')

        if not usuario_id:
            return

        try:
            from users.models import Perfil
            # Precargar rol_rbac y permisos asociados en una sola consulta optimizada
            perfil = Perfil.objects.select_related('rol_rbac').prefetch_related('rol_rbac__permisos').get(id=usuario_id)

            # Cuenta desactivada → invalidar sesión inmediatamente
            if not perfil.esta_activo:
                request.session.flush()
                return

            request.perfil_usuario = perfil
            request.permisos_usuario = list(perfil.rol_rbac.permisos.values_list('codigo', flat=True)) if perfil.rol_rbac else []

            # Sincronizar sesión (para mantener retrocompatibilidad de cookies)
            rol_en_sesion = request.session.get('rol_usuario')
            if rol_en_sesion != perfil.rol or request.session.get('usuario_id') != str(perfil.id):
                request.session['usuario_id'] = str(perfil.id)
                request.session['rol_usuario'] = perfil.rol
                request.session['permisos_usuario'] = request.permisos_usuario
                if token:
                    request.session['token_acceso'] = token
                request.session.modified = True

        except Exception as e:
            # En caso de error (por ejemplo, perfil no existe en BD), no interrumpir la petición
            pass

    def _enforce_strict_panel_isolation(self, request):
        """
        Enforce strict segregation of duties (RBAC).
        If an admin or delivery user attempts to leave their panel and access a public or client page,
        their active session is immediately flushed (closing the session) and they are redirected to '/'.
        """
        rol_sesion = request.session.get('rol_usuario')
        if not rol_sesion:
            return None

        path = request.path

        # Ignore static, media, assets, and debug toolbar
        if (path.startswith('/static/') or 
            path.startswith('/media/') or 
            path.startswith('/__debug__/') or
            path in ('/favicon.ico', '/robots.txt', '/sitemap.xml')):
            return None

        # Admin panel isolation: must only access /admin-panel/
        if rol_sesion == 'admin':
            if not path.startswith('/admin-panel/'):
                request.session.flush()
                try:
                    messages.warning(request, 'Sesión de administrador cerrada por políticas de seguridad al salir del panel.')
                except Exception:
                    pass
                return redirect('/')

        # Repartidor panel isolation: must only access /repartidor/
        elif rol_sesion == 'repartidor':
            if not path.startswith('/repartidor/'):
                request.session.flush()
                try:
                    messages.warning(request, 'Sesión de repartidor cerrada por políticas de seguridad al salir del panel.')
                except Exception:
                    pass
                return redirect('/')

        return None
