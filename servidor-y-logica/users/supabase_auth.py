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
    """Autenticar usuario con Supabase Auth o SQLite Local."""
    if getattr(settings, 'USE_SQLITE', False):
        from django.db import connection
        try:
            with connection.cursor() as cursor:
                # Asegurar existencia de la tabla local
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS "auth.users" (
                        id TEXT PRIMARY KEY,
                        email TEXT UNIQUE,
                        encrypted_password TEXT,
                        role TEXT,
                        email_confirmed_at TIMESTAMP
                    )
                    """
                )
                cursor.execute(
                    "SELECT id, email, role, encrypted_password FROM \"auth.users\" WHERE email = %s",
                    [correo]
                )
                row = cursor.fetchone()
                if row:
                    user_id, email, role, enc_pass = row
                    if enc_pass == clave:
                        return {
                            'user': {
                                'id': user_id,
                                'email': email,
                                'user_metadata': {'role': role, 'full_name': email.split('@')[0], 'username': email.split('@')[0]}
                            },
                            'access_token': 'mock-local-token'
                        }, None
                return None, "Credenciales incorrectas (Local SQLite)."
        except Exception as e:
            return None, f"Error de base de datos local: {str(e)}"

    url = f"{NUCLEO_URL_SUPABASE}/auth/v1/token?grant_type=password"
    datos, error = _hacer_peticion(url, {'email': correo, 'password': clave})
    return datos, error


def registrar_usuario(correo, clave, nombre_completo, nombre_usuario, rol='client'):
    """Registrar un nuevo usuario en Supabase Auth o SQLite Local."""
    if getattr(settings, 'USE_SQLITE', False):
        from django.db import connection
        import uuid
        user_id = str(uuid.uuid4())
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS "auth.users" (
                        id TEXT PRIMARY KEY,
                        email TEXT UNIQUE,
                        encrypted_password TEXT,
                        role TEXT,
                        email_confirmed_at TIMESTAMP
                    )
                    """
                )
                cursor.execute(
                    "INSERT INTO \"auth.users\" (id, email, encrypted_password, role, email_confirmed_at) VALUES (%s, %s, %s, %s, datetime('now'))",
                    [user_id, correo, clave, rol]
                )
            return {
                'user': {
                    'id': user_id,
                    'email': correo,
                    'user_metadata': {'full_name': nombre_completo, 'username': nombre_usuario, 'role': rol}
                },
                'access_token': 'mock-local-token'
            }, None
        except Exception as e:
            return None, f"Error al registrar usuario local: {str(e)}"

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
    if getattr(settings, 'USE_SQLITE', False):
        return registrar_usuario(correo, clave, nombre_completo, nombre_usuario, rol)

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


def subir_a_supabase_storage(nombre_archivo, datos_archivo, content_type=None):
    """
    Sube un archivo al bucket 'mikitech' de Supabase Storage.
    Retorna la URL pública del archivo si es exitoso, o None y el error si falla.
    """
    import mimetypes
    url = f"{NUCLEO_URL_SUPABASE}/storage/v1/object/mikitech/{nombre_archivo}"
    
    # MIME type guess if not provided
    mime = content_type
    if not mime:
        mime = mimetypes.guess_type(nombre_archivo)[0] or 'application/octet-stream'
        
    cabeceras = {
        'apikey': CLAVE_SUPABASE,
        'Authorization': f'Bearer {CLAVE_SUPABASE}',
        'Content-Type': mime
    }
    
    # Realizar petición POST (creación)
    req = urllib.request.Request(url, data=datos_archivo, headers=cabeceras, method='POST')
    
    try:
        with urllib.request.urlopen(req) as respuesta:
            public_url = f"{NUCLEO_URL_SUPABASE}/storage/v1/object/public/mikitech/{nombre_archivo}"
            return public_url, None
    except urllib.error.HTTPError as e:
        # Si ya existe (400/409), intentar actualizar con PUT
        if e.code in [400, 409]:
            req_update = urllib.request.Request(url, data=datos_archivo, headers=cabeceras, method='PUT')
            try:
                with urllib.request.urlopen(req_update) as respuesta:
                    public_url = f"{NUCLEO_URL_SUPABASE}/storage/v1/object/public/mikitech/{nombre_archivo}"
                    return public_url, None
            except Exception as ex:
                return None, f"Error al sobreescribir en storage: {str(ex)}"
        try:
            cuerpo_error = json.loads(e.read().decode('utf-8'))
            mensaje = cuerpo_error.get('error') or cuerpo_error.get('message') or str(e)
        except Exception:
            mensaje = str(e)
        return None, f"Error HTTP {e.code} en storage: {mensaje}"
    except Exception as e:
        return None, f"Error inesperado de red en storage: {str(e)}"
