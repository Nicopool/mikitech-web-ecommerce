from functools import wraps
from django.shortcuts import redirect

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
