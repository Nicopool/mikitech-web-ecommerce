"""
Middleware de seguridad — MIKITECH

Previene que el navegador muestre páginas cacheadas tras cerrar sesión.
Cuando el usuario presiona "Atrás" después del logout, el navegador
DEBE re-solicitar la página al servidor (que verificará la sesión).
"""


class NoCacheMiddleware:
    """
    Agrega headers Cache-Control a las rutas protegidas (/cuenta/, /admin-panel/)
    para que el navegador no muestre páginas desde caché tras cerrar sesión.
    """

    RUTAS_PROTEGIDAS = ('/cuenta', '/admin-panel')

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
