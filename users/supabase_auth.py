"""Servicio de autenticación con la API REST de Supabase"""

import json
import urllib.request
import urllib.error
from django.conf import settings


NUCLEO_URL_SUPABASE = settings.SUPABASE_URL
CLAVE_SUPABASE = settings.SUPABASE_ANON_KEY


def _hacer_peticion(url, datos=None, metodo='POST', token=None):
    """Realiza una petición HTTP a la API de Supabase."""
    cabeceras = {
        'Content-Type': 'application/json',
        'apikey': CLAVE_SUPABASE,
        'Authorization': f'Bearer {token if token else CLAVE_SUPABASE}'
    }

    cuerpo = json.dumps(datos).encode('utf-8') if datos else None
    peticion = urllib.request.Request(url, data=cuerpo, headers=cabeceras, method=metodo)

    try:
        with urllib.request.urlopen(peticion) as respuesta:
            return json.loads(respuesta.read().decode('utf-8')), None
    except urllib.error.HTTPError as e:
        cuerpo_error = json.loads(e.read().decode('utf-8'))
        mensaje_error = cuerpo_error.get('error_description') or cuerpo_error.get('msg') or 'Error desconocido'
        return None, mensaje_error
    except Exception as e:
        return None, str(e)


def iniciar_sesion_usuario(correo, clave):
    """Autenticar usuario con Supabase Auth."""
    url = f"{NUCLEO_URL_SUPABASE}/auth/v1/token?grant_type=password"
    datos, error = _hacer_peticion(url, {'email': correo, 'password': clave})
    return datos, error


def registrar_usuario(correo, clave, nombre_completo, nombre_usuario, rol='client'):
    """Registrar un nuevo usuario en Supabase Auth."""
    url = f"{NUCLEO_URL_SUPABASE}/auth/v1/signup"
    datos, error = _hacer_peticion(url, {
        'email': correo,
        'password': clave,
        'data': {
            'full_name': nombre_completo,
            'username': nombre_usuario,
            'role': rol
        }
    })
    return datos, error


def registrar_usuario_sql(correo, clave, nombre_completo, nombre_usuario, rol='client'):
    """
    Fallback: Registrar un usuario directamente en la tabla auth.users vía SQL.
    Se usa cuando Supabase no puede enviar correos de confirmación (error de SMTP).
    """
    from django.db import connection
    import json
    import uuid

    id_usuario = str(uuid.uuid4())
    metadata_usuario = json.dumps({
        'full_name': nombre_completo,
        'username': nombre_usuario,
        'role': rol
    })
    metadata_app = json.dumps({
        'provider': 'email',
        'providers': ['email']
    })

    query = """
        INSERT INTO auth.users (
            id, instance_id, email, encrypted_password, email_confirmed_at, 
            raw_app_meta_data, raw_user_meta_data, created_at, updated_at, 
            aud, role, is_super_admin, phone_confirmed_at, 
            confirmation_token, recovery_token, email_change_token_new, email_change
        )
        VALUES (
            %s, '00000000-0000-0000-0000-000000000000', %s, crypt(%s, gen_salt('bf')), NOW(), 
            %s, %s, NOW(), NOW(), 
            'authenticated', 'authenticated', false, NOW(),
            '', '', '', ''
        )
        RETURNING id;
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [id_usuario, correo, clave, metadata_app, metadata_usuario])
            row = cursor.fetchone()
            if row:
                return {'user': {'id': str(row[0])}}, None
            return None, "Error al insertar el usuario en la base de datos."
    except Exception as e:
        return None, str(e)


def actualizar_contraseña(token, nueva_clave):
    """Actualizar la contraseña del usuario en Supabase."""
    url = f"{NUCLEO_URL_SUPABASE}/auth/v1/user"
    datos, error = _hacer_peticion(url, {'password': nueva_clave}, token)
    return datos, error


def obtener_usuario_por_token(token):
    """Obtener los datos del usuario autenticado mediante su token."""
    url = f"{NUCLEO_URL_SUPABASE}/auth/v1/user"
    datos, error = _hacer_peticion(url, metodo='GET', token=token)
    return datos, error


def enviar_recuperacion_contraseña(correo):
    """Solicita un correo de recuperación de contraseña."""
    url = f"{NUCLEO_URL_SUPABASE}/auth/v1/recover"
    datos, error = _hacer_peticion(url, {'email': correo})
    return datos, error


def verificar_otp_recuperacion(correo, token_otp, nueva_clave):
    """Verifica el código OTP enviado por correo y actualiza la contraseña."""
    # 1. Verificar el token OTP
    url_verificacion = f"{NUCLEO_URL_SUPABASE}/auth/v1/verify"
    datos_verificacion, error_verificacion = _hacer_peticion(url_verificacion, {
        'type': 'recovery',
        'email': correo,
        'token': token_otp
    })
    
    if error_verificacion:
        return None, error_verificacion
        
    token_acceso = datos_verificacion.get('access_token')
    if not token_acceso:
        return None, "Error al validar el código OTP."
        
    # 2. Actualizar la contraseña usando el token_acceso obtenido
    url_actualizacion = f"{NUCLEO_URL_SUPABASE}/auth/v1/user"
    datos_actualizacion, error_actualizacion = _hacer_peticion(
        url_actualizacion, 
        datos={'password': nueva_clave}, 
        metodo='PUT', 
        token=token_acceso
    )
    
    if error_actualizacion:
        return None, error_actualizacion
        
    return datos_actualizacion, None
