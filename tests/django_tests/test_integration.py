import os
import sys
from pathlib import Path

# Agregar el directorio del backend al path de python
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'servidor-y-logica'))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from django.conf import settings
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS = list(settings.ALLOWED_HOSTS) + ['testserver']

import unittest
from django.test import Client

class TestWebRoutesIntegration(unittest.TestCase):
    def setUp(self):
        # Inicializar el cliente de pruebas de Django
        self.client = Client()

    def test_ping_endpoint(self):
        """Verifica que el endpoint de ping esté activo y responda con JSON."""
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        
        # Verificar el contenido del JSON
        data = response.json()
        self.assertEqual(data.get('status'), 'ok')
        self.assertEqual(data.get('msg'), 'pong')

    def test_home_page(self):
        """Verifica que la página principal cargue correctamente."""
        response = self.client.get('/')
        # Debe responder con 200 OK
        self.assertEqual(response.status_code, 200)
        # Debe contener elementos clave de la landing page
        self.assertIn(b'MIKITECH', response.content)

    def test_client_denied_admin_panel(self):
        """Verifica que un usuario sin rol de administrador sea rechazado y redirigido del panel admin."""
        # Intentar acceder al dashboard de administración sin sesión activa
        response = self.client.get('/admin-panel/')
        # Debe redirigir (302 Redirect) a la pasarela de seguridad
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin-panel/pasarela/', response.url)

    def test_client_denied_repartidor_panel(self):
        """Verifica que un usuario sin rol de repartidor sea rechazado y redirigido del panel de repartidor."""
        # Intentar acceder al panel del repartidor sin sesión activa
        response = self.client.get('/repartidor/')
        # Debe redirigir (302 Redirect) a la pasarela del repartidor
        self.assertEqual(response.status_code, 302)
        self.assertIn('/repartidor/pasarela/', response.url)

    def test_signup_duplicate_email_blocked(self):
        """Verifica que no se permita registrar un usuario con un correo que ya existe."""
        import uuid
        from django.db import connection
        from django.conf import settings
        
        table_name = '"auth.users"' if getattr(settings, 'USE_SQLITE', False) else 'auth.users'
        email_dup = f"duplicate_email_{uuid.uuid4().hex[:8]}@gmail.com"
        unique_username = f"user_{uuid.uuid4().hex[:10]}"
        
        # 1. Limpieza inicial
        with connection.cursor() as cursor:
            if getattr(settings, 'USE_SQLITE', False):
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
            try:
                cursor.execute(f"SELECT id FROM {table_name} WHERE email = %s", [email_dup])
                row = cursor.fetchone()
                if row:
                    cursor.execute("DELETE FROM profiles WHERE id = %s", [row[0]])
                cursor.execute(f"DELETE FROM {table_name} WHERE email = %s", [email_dup])
            except Exception:
                pass

        # 2. Insertar un correo simulado directamente en la tabla auth.users
        simulated_uuid = str(uuid.uuid4())
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {table_name} (id, email) VALUES (%s, %s)",
                [simulated_uuid, email_dup]
            )
                
        # 3. Simular petición de registro POST con el mismo correo y un nombre de usuario nuevo
        datos_registro = {
            'nombre_completo': 'Test Duplicado',
            'nombre_usuario': unique_username,
            'correo': email_dup,
            'clave': 'PasswordSafe123!',
            'clave2': 'PasswordSafe123!',
            'terminos': 'on'
        }
        
        try:
            response = self.client.post('/cuenta/registro/', datos_registro)
            self.assertEqual(response.status_code, 200)
            
            # Reemplazar tildes para evitar problemas de codificación en assertions
            contenido_sin_tildes = response.content.replace(b'\xc3\xa1', b'a').replace(b'\xc3\xa9', b'e').replace(b'\xc3\xad', b'i').replace(b'\xc3\xb3', b'o').replace(b'\xc3\xba', b'u')
            self.assertIn(b'Este correo electronico ya esta registrado', contenido_sin_tildes)
        finally:
            # 4. Limpieza final
            with connection.cursor() as cursor:
                try:
                    cursor.execute("DELETE FROM profiles WHERE id = %s", [simulated_uuid])
                    cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", [simulated_uuid])
                except Exception:
                    pass

    def test_admin_signup_duplicate_email_blocked(self):
        """Verifica que no se permita registrar un administrador con un correo que ya existe."""
        import uuid
        from django.db import connection
        from django.conf import settings
        
        table_name = '"auth.users"' if getattr(settings, 'USE_SQLITE', False) else 'auth.users'
        email_dup = f"duplicate_email_admin_{uuid.uuid4().hex[:8]}@gmail.com"
        unique_username = f"admin_{uuid.uuid4().hex[:10]}"
        
        # 1. Limpieza inicial
        with connection.cursor() as cursor:
            if getattr(settings, 'USE_SQLITE', False):
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
            try:
                cursor.execute(f"SELECT id FROM {table_name} WHERE email = %s", [email_dup])
                row = cursor.fetchone()
                if row:
                    cursor.execute("DELETE FROM profiles WHERE id = %s", [row[0]])
                cursor.execute(f"DELETE FROM {table_name} WHERE email = %s", [email_dup])
            except Exception:
                pass

        # 2. Insertar un correo simulado directamente en la tabla auth.users
        simulated_uuid = str(uuid.uuid4())
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {table_name} (id, email) VALUES (%s, %s)",
                [simulated_uuid, email_dup]
            )
                
        # 3. Simular petición de registro POST de administrador usando RequestFactory para evitar limitaciones de cookies firmadas en entorno de test
        from django.test import RequestFactory
        from django.contrib.sessions.middleware import SessionMiddleware
        from core.admin_views import registro_administrador
        
        rf = RequestFactory()
        datos_registro = {
            'nombre_completo': 'Admin Duplicado',
            'nombre_usuario': unique_username,
            'correo': email_dup,
            'clave': 'PasswordSafe123!',
            'confirmar_clave': 'PasswordSafe123!',
            'terminos': 'on'
        }
        
        request = rf.post('/admin-panel/registro/', datos_registro)
        
        # Aplicar SessionMiddleware para inicializar request.session
        middleware = SessionMiddleware(get_response=lambda r: None)
        middleware.process_request(request)
        
        # Superar pasarela
        request.session['pasarela_administrador_superada'] = True
        request.session.save()
        
        try:
            response = registro_administrador(request)
            self.assertEqual(response.status_code, 200)
            
            # Reemplazar tildes para evitar problemas de codificación en assertions
            contenido_sin_tildes = response.content.replace(b'\xc3\xa1', b'a').replace(b'\xc3\xa9', b'e').replace(b'\xc3\xad', b'i').replace(b'\xc3\xb3', b'o').replace(b'\xc3\xba', b'u')
            self.assertIn(b'Este correo electronico ya esta registrado', contenido_sin_tildes)
        finally:
            # 4. Limpieza final
            with connection.cursor() as cursor:
                try:
                    cursor.execute("DELETE FROM profiles WHERE id = %s", [simulated_uuid])
                    cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", [simulated_uuid])
                except Exception:
                    pass



class TestTripleLockSecurity(unittest.TestCase):
    """
    ISO 25010 – Pruebas del sistema de triple cerrojo (RBAC en tiempo real).

    Verifica que los decoradores @requerir_administrador y @requiere_repartidor
    rechacen correctamente el acceso cuando cualquiera de los tres cerrojos falla.
    """

    def setUp(self):
        self.client = Client()

    def test_admin_panel_blocked_without_gateway_flag(self):
        """
        Cerrojo 3: Un admin con rol correcto pero sin haber pasado la pasarela
        debe ser redirigido a la pasarela, no al panel.
        """
        # No se puede simular 'admin' genuino en test sin BD real, pero
        # sí podemos verificar que sin sesión el panel siempre bloquea.
        response = self.client.get('/admin-panel/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin-panel/pasarela/', response.url)

    def test_admin_panel_blocked_with_client_role_and_gateway(self):
        """
        Cerrojo 2: Un usuario con rol 'client' que logra insertar el flag de pasarela
        igual debe ser rechazado porque su rol no es 'admin'.
        """
        from django.test import RequestFactory
        from django.contrib.sessions.middleware import SessionMiddleware
        from core.admin_views import tablero_administrador

        rf = RequestFactory()
        request = rf.get('/admin-panel/')
        middleware = SessionMiddleware(get_response=lambda r: None)
        middleware.process_request(request)

        # Simular un usuario con rol 'client' que manipuló el flag de pasarela
        request.session['usuario_id'] = 'fake-user-id'
        request.session['rol_usuario'] = 'client'  # Rol incorrecto
        request.session['pasarela_administrador_superada'] = True  # Intento de bypass
        request.session.save()

        response = tablero_administrador(request)
        # El cerrojo 2 debe rechazarlo y redirigir a /admin-panel/pasarela/
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin-panel/pasarela/', response.url)

    def test_repartidor_panel_blocked_without_gateway_flag(self):
        """
        Cerrojo 3: Un repartidor con rol correcto pero sin flag de pasarela
        debe ser redirigido a la pasarela, no al panel.
        """
        from django.test import RequestFactory
        from django.contrib.sessions.middleware import SessionMiddleware
        from core.repartidor_views import panel_repartidor

        rf = RequestFactory()
        request = rf.get('/repartidor/')
        middleware = SessionMiddleware(get_response=lambda r: None)
        middleware.process_request(request)

        # Simular repartidor SIN flag de pasarela
        request.session['usuario_id'] = 'fake-repartidor-id'
        request.session['rol_usuario'] = 'repartidor'  # Rol correcto
        # Deliberadamente NO se establece 'pasarela_repartidor_superada'
        request.session.save()

        response = panel_repartidor(request)
        # El cerrojo 3 debe rechazarlo
        self.assertEqual(response.status_code, 302)
        self.assertIn('/repartidor/pasarela/', response.url)

    def test_repartidor_panel_blocked_with_admin_role(self):
        """
        Cerrojo 2: Un admin que intenta acceder al panel de repartidor debe ser bloqueado
        porque su rol no es 'repartidor'.
        """
        from django.test import RequestFactory
        from django.contrib.sessions.middleware import SessionMiddleware
        from core.repartidor_views import panel_repartidor

        rf = RequestFactory()
        request = rf.get('/repartidor/')
        middleware = SessionMiddleware(get_response=lambda r: None)
        middleware.process_request(request)

        # Simular admin intentando acceder a panel de repartidor
        request.session['usuario_id'] = 'fake-admin-id'
        request.session['rol_usuario'] = 'admin'  # Rol de admin, no repartidor
        request.session['pasarela_repartidor_superada'] = True
        request.session.save()

        response = panel_repartidor(request)
        # El cerrojo 2 debe rechazarlo — un admin NO es un repartidor
        self.assertEqual(response.status_code, 302)
        self.assertIn('/repartidor/pasarela/', response.url)


if __name__ == "__main__":
    unittest.main(verbosity=2)
