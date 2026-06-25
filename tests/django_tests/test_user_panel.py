import os
import sys
from pathlib import Path

# Agregar el directorio del backend al path de python
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from django.conf import settings
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS = list(settings.ALLOWED_HOSTS) + ['testserver']

import unittest
import uuid
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
from django.db import connection
from users.models import Perfil

class TestUserPanelIntegration(unittest.TestCase):
    def setUp(self):
        self.user_uuid = str(uuid.uuid4())
        self.username = f"user_{uuid.uuid4().hex[:10]}"
        self.email = f"user_{self.username}@mikitech.test"

        # Asegurar que existan las tablas mock en SQLite para pruebas
        if getattr(settings, 'USE_SQLITE', False):
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS "auth.users" (
                        id TEXT PRIMARY KEY,
                        email TEXT UNIQUE,
                        encrypted_password TEXT,
                        role TEXT,
                        email_confirmed_at TIMESTAMP
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS profiles (
                        id TEXT PRIMARY KEY,
                        full_name TEXT,
                        username TEXT UNIQUE,
                        bio TEXT,
                        avatar_url TEXT,
                        phone TEXT,
                        address TEXT,
                        city TEXT,
                        country TEXT DEFAULT 'Colombia',
                        role TEXT DEFAULT 'client',
                        is_active INTEGER DEFAULT 1,
                        created_at TIMESTAMP,
                        updated_at TIMESTAMP
                    )
                """)
                
                # Insertar usuario simulado en auth.users
                cursor.execute(
                    'INSERT OR IGNORE INTO "auth.users" (id, email) VALUES (%s, %s)',
                    [self.user_uuid, self.email]
                )

        # Crear perfil correspondiente en la base de datos
        self.perfil, _ = Perfil.objects.get_or_create(
            id=self.user_uuid,
            defaults={
                'nombre_completo': 'Cliente Prueba',
                'nombre_usuario': self.username,
                'rol': 'client',
                'biografia': 'Entusiasta de la tecnología',
                'telefono': '123456789',
                'ciudad': 'Bogotá',
                'pais': 'Colombia'
            }
        )

    def tearDown(self):
        # Limpieza de registros de prueba
        try:
            Perfil.objects.filter(id=self.user_uuid).delete()
            if getattr(settings, 'USE_SQLITE', False):
                with connection.cursor() as cursor:
                    cursor.execute('DELETE FROM "auth.users" WHERE id = %s', [self.user_uuid])
        except Exception:
            pass

    def get_view_response(self, view_func, path, method='GET', data=None, user_id=None, role=None):
        """Helper para inicializar el request con sesión y mensajería, evitando limitaciones de cookies firmadas."""
        rf = RequestFactory()
        if method == 'POST':
            request = rf.post(path, data or {})
        else:
            request = rf.get(path)
            
        # Inicializar sesión
        session_middleware = SessionMiddleware(get_response=lambda r: None)
        session_middleware.process_request(request)
        
        if user_id:
            request.session['usuario_id'] = user_id
        if role:
            request.session['rol_usuario'] = role
            
        request.session.save()
        
        # Inicializar almacenamiento de mensajes (Django messages framework)
        request._messages = FallbackStorage(request)
        
        # Ejecutar el middleware de verificación de rol si es ruta protegida
        from core.middleware import RoleVerificationMiddleware
        role_middleware = RoleVerificationMiddleware(get_response=lambda r: None)
        response = role_middleware(request)
        if response:
            return response
            
        # Llamar a la vista directamente
        return view_func(request)

    def test_anonymous_redirected_from_user_panel_routes(self):
        """Verifica que un usuario no autenticado sea redirigido a login al intentar entrar a cualquier vista del panel."""
        from users import views
        rutas_y_vistas = [
            ('/cuenta/perfil/', views.mi_perfil),
            ('/cuenta/perfil/editar/', views.editar_perfil),
            ('/cuenta/favoritos/', views.mis_favoritos),
            ('/cuenta/pedidos/', views.mis_pedidos),
            ('/cuenta/historial/', views.mi_historial),
            ('/cuenta/reportes/', views.mis_reportes)
        ]
        for ruta, vista in rutas_y_vistas:
            response = self.get_view_response(view_func=vista, path=ruta)
            self.assertEqual(response.status_code, 302, f"Ruta {ruta} no redirigió a un usuario anónimo.")
            self.assertIn('/cuenta/ingreso/', response.url)

    def test_authenticated_client_access_profile_dashboard(self):
        """Verifica que un cliente autenticado pueda acceder a su perfil principal."""
        from users.views import mi_perfil
        response = self.get_view_response(
            view_func=mi_perfil,
            path='/cuenta/perfil/',
            user_id=self.user_uuid,
            role='client'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cliente Prueba', response.content)

    def test_authenticated_client_access_edit_profile(self):
        """Verifica que un cliente autenticado pueda acceder al formulario de edición de perfil."""
        from users.views import editar_perfil
        response = self.get_view_response(
            view_func=editar_perfil,
            path='/cuenta/perfil/editar/',
            user_id=self.user_uuid,
            role='client'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Editar Perfil', response.content)

    def test_client_edit_profile_post_successful(self):
        """Verifica que el cliente pueda guardar modificaciones en su perfil exitosamente."""
        from users.views import editar_perfil
        datos_edicion = {
            'nombre_completo': 'Juan Perez Modificado',
            'biografia': 'Nueva biografía de hardware',
            'telefono': '987654321',
            'ciudad': 'Medellín',
            'pais': 'Colombia'
        }

        response = self.get_view_response(
            view_func=editar_perfil,
            path='/cuenta/perfil/editar/',
            method='POST',
            data=datos_edicion,
            user_id=self.user_uuid,
            role='client'
        )
        
        # Debe redirigir de vuelta al perfil (302)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/cuenta/perfil/', response.url)

        # Verificar cambios guardados en la BD
        perfil_actualizado = Perfil.objects.get(id=self.user_uuid)
        self.assertEqual(perfil_actualizado.nombre_completo, 'Juan Perez Modificado')
        self.assertEqual(perfil_actualizado.biografia, 'Nueva biografía de hardware')
        self.assertEqual(perfil_actualizado.telefono, '987654321')
        self.assertEqual(perfil_actualizado.ciudad, 'Medellín')

    def test_authenticated_client_access_favorites(self):
        """Verifica que un cliente autenticado pueda acceder a su sección de favoritos."""
        from users.views import mis_favoritos
        response = self.get_view_response(
            view_func=mis_favoritos,
            path='/cuenta/favoritos/',
            user_id=self.user_uuid,
            role='client'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mis Favoritos', response.content)

    def test_authenticated_client_access_orders(self):
        """Verifica que un cliente autenticado pueda acceder a su listado de pedidos."""
        from users.views import mis_pedidos
        response = self.get_view_response(
            view_func=mis_pedidos,
            path='/cuenta/pedidos/',
            user_id=self.user_uuid,
            role='client'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mis Pedidos', response.content)

    def test_authenticated_client_access_history(self):
        """Verifica que un cliente autenticado pueda acceder a su historial."""
        from users.views import mi_historial
        response = self.get_view_response(
            view_func=mi_historial,
            path='/cuenta/historial/',
            user_id=self.user_uuid,
            role='client'
        )
        self.assertEqual(response.status_code, 200)

    def test_authenticated_client_access_reports(self):
        """Verifica que un cliente autenticado pueda acceder a su sección de reportes."""
        from users.views import mis_reportes
        response = self.get_view_response(
            view_func=mis_reportes,
            path='/cuenta/reportes/',
            user_id=self.user_uuid,
            role='client'
        )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
