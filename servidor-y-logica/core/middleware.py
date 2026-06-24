"""
Middleware de seguridad — MIKITECH

NoCacheMiddleware: Previene que el navegador muestre páginas cacheadas tras cerrar sesión.
RoleVerificationMiddleware: Sincroniza el rol de sesión con la base de datos en cada
                            petición, evitando que una sesión obsoleta conserve privilegios
                            elevados tras una degradación de rol (ISO 25010 – Seguridad).
"""


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
        return self.get_response(request)

    def _verificar_y_sincronizar_rol(self, request):
        """Sincroniza el rol de sesión con el valor actual en la base de datos."""
        # Solo actuar en rutas protegidas
        if not any(request.path.startswith(ruta) for ruta in self.RUTAS_VERIFICACION):
            return

        # No verificar en rutas de acceso público (login, pasarela, registro)
        if any(request.path.startswith(ruta) for ruta in self.RUTAS_EXCLUIDAS):
            return

        usuario_id = request.session.get('usuario_id')
        if not usuario_id:
            return

        try:
            from users.models import Perfil
            perfil = Perfil.objects.only('rol', 'esta_activo').get(id=usuario_id)

            # Cuenta desactivada → invalidar sesión inmediatamente
            if not perfil.esta_activo:
                request.session.flush()
                return

            # Sincronizar el rol con el valor real de la base de datos
            rol_en_sesion = request.session.get('rol_usuario')
            if rol_en_sesion != perfil.rol:
                request.session['rol_usuario'] = perfil.rol
                request.session.modified = True

        except Exception:
            # Si el perfil no existe o hay error de BD, no interrumpir la petición
            # — los decoradores individuales se encargarán de redirigir si hace falta
            pass
