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
from django.test import RequestFactory, Client
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
from django.db import connection
from django.http import HttpResponse, JsonResponse
from users.models import Perfil, Rol, Permiso
from users.decorators import requiere_permiso
from core.middleware import RoleVerificationMiddleware


@requiere_permiso('crear_producto')
def dummy_create_product_view(request):
    return HttpResponse("Producto creado exitosamente")


@requiere_permiso('ver_reportes')
def dummy_view_reports_view(request):
    return HttpResponse("Reportes cargados")


class TestRBACIntegration(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.rf = RequestFactory()
        
        # Generar IDs únicos para la prueba
        self.client_uuid = str(uuid.uuid4())
        self.admin_uuid = str(uuid.uuid4())
        self.repartidor_uuid = str(uuid.uuid4())
        
        # Asegurar tablas mock de Supabase en SQLite
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
                        role_id TEXT,
                        role TEXT DEFAULT 'client',
                        is_active INTEGER DEFAULT 1,
                        created_at TIMESTAMP,
                        updated_at TIMESTAMP
                    )
                """)
                # Insertar mock auth records
                cursor.execute('INSERT OR IGNORE INTO "auth.users" (id, email) VALUES (%s, %s)', [self.client_uuid, 'client@rbac.test'])
                cursor.execute('INSERT OR IGNORE INTO "auth.users" (id, email) VALUES (%s, %s)', [self.admin_uuid, 'admin@rbac.test'])
                cursor.execute('INSERT OR IGNORE INTO "auth.users" (id, email) VALUES (%s, %s)', [self.repartidor_uuid, 'repartidor@rbac.test'])

        # Obtener o crear Roles y Permisos (ya deberían estar poblados por migración 0003, pero garantizamos su existencia)
        self.permiso_crear = Permiso.objects.get_or_create(codigo='crear_producto', defaults={'nombre': 'Crear Producto'})[0]
        self.permiso_reportes = Permiso.objects.get_or_create(codigo='ver_reportes', defaults={'nombre': 'Ver Reportes'})[0]
        
        self.rol_client = Rol.objects.get_or_create(codigo='client', defaults={'nombre': 'Cliente'})[0]
        self.rol_admin = Rol.objects.get_or_create(codigo='admin', defaults={'nombre': 'Administrador'})[0]
        self.rol_repartidor = Rol.objects.get_or_create(codigo='repartidor', defaults={'nombre': 'Repartidor'})[0]

        # Crear Perfiles de prueba asociados a sus respectivos roles
        self.perfil_client, _ = Perfil.objects.get_or_create(
            id=self.client_uuid,
            defaults={
                'nombre_completo': 'Cliente Prueba RBAC',
                'nombre_usuario': 'client_rbac',
                'rol_rbac': self.rol_client,
                'esta_activo': True
            }
        )
        self.perfil_admin, _ = Perfil.objects.get_or_create(
            id=self.admin_uuid,
            defaults={
                'nombre_completo': 'Admin Prueba RBAC',
                'nombre_usuario': 'admin_rbac',
                'rol_rbac': self.rol_admin,
                'esta_activo': True
            }
        )
        self.perfil_repartidor, _ = Perfil.objects.get_or_create(
            id=self.repartidor_uuid,
            defaults={
                'nombre_completo': 'Repartidor Prueba RBAC',
                'nombre_usuario': 'driver_rbac',
                'rol_rbac': self.rol_repartidor,
                'esta_activo': True
            }
        )

    def tearDown(self):
        # Limpieza de registros creados
        Perfil.objects.filter(id__in=[self.client_uuid, self.admin_uuid, self.repartidor_uuid]).delete()
        if getattr(settings, 'USE_SQLITE', False):
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM "auth.users" WHERE id IN (%s, %s, %s)', [self.client_uuid, self.admin_uuid, self.repartidor_uuid])

    def get_mock_request(self, path, method='GET', user_id=None, role=None, headers=None):
        """Helper para construir un request mock con middleware configurado."""
        if method == 'POST':
            request = self.rf.post(path)
        else:
            request = self.rf.get(path)
            
        if headers:
            for k, v in headers.items():
                request.META[f"HTTP_{k.upper().replace('-', '_')}"] = v

        # Configurar SessionMiddleware
        session_middleware = SessionMiddleware(get_response=lambda r: None)
        session_middleware.process_request(request)
        
        if user_id:
            request.session['usuario_id'] = user_id
        if role:
            request.session['rol_usuario'] = role
            
        request.session.save()
        request._messages = FallbackStorage(request)
        return request

    def test_role_model_bidirectional_sync(self):
        """Verifica que el campo Perfil.rol (CharField legacy) y Perfil.rol_rbac se sincronicen bidireccionalmente."""
        # 1. Crear perfil especificando solo rol_rbac. Debe autocompletar el rol CharField legacy.
        p1 = Perfil(id=str(uuid.uuid4()), nombre_usuario='sync_test_1', rol_rbac=self.rol_admin)
        p1.save()
        self.assertEqual(p1.rol, 'admin')
        p1.delete()

        # 2. Crear perfil especificando solo rol CharField legacy. Debe autocompletar el rol_rbac ForeignKey.
        p2 = Perfil(id=str(uuid.uuid4()), nombre_usuario='sync_test_2', rol='client')
        p2.save()
        self.assertEqual(p2.rol_rbac, self.rol_client)
        p2.delete()

    def test_requiere_permiso_decorator_denies_unauthorized(self):
        """Verifica que un usuario sin el permiso requerido sea rechazado con 403 Forbidden."""
        # Cliente intenta acceder a vista que requiere 'crear_producto' (que no posee)
        request = self.get_mock_request('/admin-panel/productos/crear/', user_id=self.client_uuid, role='client')
        
        # Ejecutar middleware para poblar permisos en request.permisos_usuario
        middleware = RoleVerificationMiddleware(get_response=lambda r: None)
        middleware(request)
        
        # Llamar a la vista decorada
        response = dummy_create_product_view(request)
        
        self.assertEqual(response.status_code, 403)
        self.assertIn(b"Forbidden", response.content)

    def test_requiere_permiso_decorator_allows_authorized(self):
        """Verifica que un usuario con el permiso requerido acceda exitosamente (200 OK)."""
        # Admin intenta acceder a vista que requiere 'ver_reportes' (que posee)
        request = self.get_mock_request('/admin-panel/reportes/', user_id=self.admin_uuid, role='admin')
        
        middleware = RoleVerificationMiddleware(get_response=lambda r: None)
        middleware(request)
        
        response = dummy_view_reports_view(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Reportes cargados")

    def test_middleware_jwt_auth_role_sync(self):
        """Verifica que el middleware procese tokens JWT Bearer simulados y cargue permisos."""
        headers = {'Authorization': 'Bearer mock-local-token'}
        request = self.get_mock_request('/cuenta/perfil/', headers=headers)
        
        # Escribimos en sesión el usuario_id del admin para que el mock token lo asocie
        request.session['usuario_id'] = self.admin_uuid
        request.session.save()
        
        middleware = RoleVerificationMiddleware(get_response=lambda r: None)
        middleware(request)
        
        self.assertEqual(str(request.perfil_usuario.id), self.admin_uuid)
        self.assertIn('ver_reportes', request.permisos_usuario)
        self.assertIn('crear_producto', request.permisos_usuario)

    def test_middleware_strict_segregation(self):
        """Verifica que si un admin o repartidor sale de su panel sea desautenticado de inmediato."""
        # Caso 1: Admin intenta ingresar al panel de cliente /cuenta/perfil/
        request = self.get_mock_request('/cuenta/perfil/', user_id=self.admin_uuid, role='admin')
        
        middleware = RoleVerificationMiddleware(get_response=lambda r: None)
        response = middleware(request)
        
        # Debe haber disparado una redirección
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        
        # Su sesión debe haber sido limpiada (flush)
        self.assertIsNone(request.session.get('usuario_id'))

        # Caso 2: Repartidor intenta ingresar al panel de cliente /cuenta/perfil/
        request = self.get_mock_request('/cuenta/perfil/', user_id=self.repartidor_uuid, role='repartidor')
        
        response = middleware(request)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertIsNone(request.session.get('usuario_id'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
