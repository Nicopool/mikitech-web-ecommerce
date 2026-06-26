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
from users.models import Perfil, Rol, Permiso, InvitacionAdmin
from core.admin_views import (
    crear_invitacion_admin, 
    revocar_invitacion_admin, 
    reenviar_invitacion_admin,
    desactivar_usuario_admin,
    cambiar_contrasena_forzado
)
from core.middleware import RoleVerificationMiddleware


class TestAdminInvitations(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.rf = RequestFactory()
        
        # IDs únicos para las pruebas
        self.superadmin_uuid = str(uuid.uuid4())
        self.invite_email = f"invited_admin_{uuid.uuid4().hex[:8]}@gmail.com"
        
        # Garantizar que el rol 'admin' exista
        self.rol_admin = Rol.objects.get_or_create(codigo='admin', defaults={'nombre': 'Administrador'})[0]
        # Permiso 'gestionar_usuarios' (solo para superadmin)
        self.permiso_usuarios = Permiso.objects.get_or_create(codigo='gestionar_usuarios', defaults={'nombre': 'Gestionar Usuarios'})[0]
        
        # Crear perfil de superadmin que tiene permisos para invitar
        self.superadmin_perfil, _ = Perfil.objects.get_or_create(
            id=self.superadmin_uuid,
            defaults={
                'nombre_completo': 'Super Admin Test',
                'nombre_usuario': f'superadmin_{uuid.uuid4().hex[:6]}',
                'rol': 'admin',
                'rol_rbac': self.rol_admin,
                'esta_activo': True,
                'password_cambiada': True
            }
        )
        self.superadmin_perfil.rol_rbac.permisos.add(self.permiso_usuarios)

        # Asegurar tablas mock en SQLite para pruebas
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
                cursor.execute('INSERT OR IGNORE INTO "auth.users" (id, email) VALUES (%s, %s)', [self.superadmin_uuid, 'superadmin@mikitech.test'])

    def tearDown(self):
        # Limpieza
        Perfil.objects.filter(id=self.superadmin_uuid).delete()
        
        # Buscar invitaciones creadas y limpiar perfiles y auth correspondientes
        invs = InvitacionAdmin.objects.filter(email=self.invite_email)
        for inv in invs:
            Perfil.objects.filter(invitacion=inv).delete()
        invs.delete()
        
        if getattr(settings, 'USE_SQLITE', False):
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM "auth.users" WHERE id = %s', [self.superadmin_uuid])
                cursor.execute('DELETE FROM "auth.users" WHERE email = %s', [self.invite_email])

    def get_mock_request(self, path, method='GET', post_data=None, user_id=None, role=None, permissions=None):
        """Helper para construir un request mock con middleware y perfil precargado."""
        if method == 'POST':
            request = self.rf.post(path, post_data or {})
        else:
            request = self.rf.get(path)

        # Session
        session_middleware = SessionMiddleware(get_response=lambda r: None)
        session_middleware.process_request(request)
        
        if user_id:
            request.session['usuario_id'] = user_id
        if role:
            request.session['rol_usuario'] = role
        request.session.save()
        
        # Messages
        request._messages = FallbackStorage(request)
        
        # Precargar en middleware
        request.perfil_usuario = Perfil.objects.filter(id=user_id).first() if user_id else None
        request.permisos_usuario = permissions or []
        
        return request

    def test_public_registration_redirects(self):
        """Verifica que el registro público de administradores esté inhabilitado y retorne 404."""
        response = self.client.get('/admin-panel/registro/')
        self.assertEqual(response.status_code, 404)

    def test_create_invitation_success(self):
        """Verifica que un superadmin pueda invitar a un nuevo admin y se guarden sus datos."""
        post_data = {
            'email': self.invite_email,
            'nombre_completo': 'Pedro Perez',
            'notas_internas': 'Notas de prueba de invitación'
        }
        request = self.get_mock_request(
            '/admin-panel/invitaciones/crear/',
            method='POST',
            post_data=post_data,
            user_id=self.superadmin_uuid,
            role='admin',
            permissions=['gestionar_usuarios']
        )
        
        response = crear_invitacion_admin(request)
        
        # Debe redirigir al listado de invitaciones
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/admin-panel/invitaciones/')
        
        # Validar base de datos
        inv = InvitacionAdmin.objects.filter(email=self.invite_email).first()
        self.assertIsNotNone(inv)
        self.assertEqual(inv.estado, 'pendiente')
        self.assertEqual(inv.nombre_completo, 'Pedro Perez')
        self.assertTrue(inv.usuario_generado.startswith('admin_pedrop'))
        
        # Validar perfil asociado
        perfil_invitado = Perfil.objects.filter(invitacion=inv).first()
        self.assertIsNotNone(perfil_invitado)
        self.assertEqual(perfil_invitado.rol, 'admin')
        self.assertEqual(perfil_invitado.rol_rbac.codigo, 'admin')
        self.assertFalse(perfil_invitado.password_cambiada)
        self.assertTrue(perfil_invitado.esta_activo)

    def test_forced_password_change_middleware(self):
        """Verifica que el middleware obligue a cambiar la contraseña a un administrador invitado."""
        # 1. Crear la invitación primero
        inv = InvitacionAdmin.objects.create(
            email=self.invite_email,
            nombre_completo='Pedro Perez',
            usuario_generado='admin_pedrop_9999',
            password_temporal_hash='pbkdf2_sha256$...',
            fecha_expiracion=django.utils.timezone.now() + django.utils.timezone.timedelta(days=7),
            estado='pendiente'
        )
        
        # 2. Crear su perfil con password_cambiada = False
        invited_uuid = str(uuid.uuid4())
        perfil_invitado = Perfil.objects.create(
            id=invited_uuid,
            nombre_completo='Pedro Perez',
            nombre_usuario='admin_pedrop_9999',
            rol='admin',
            rol_rbac=self.rol_admin,
            invitacion=inv,
            password_cambiada=False,
            esta_activo=True
        )

        try:
            # 3. Simular request de acceso al dashboard principal administrativo
            request = self.get_mock_request('/admin-panel/', user_id=invited_uuid, role='admin')
            
            # Instanciar y ejecutar middleware
            middleware = RoleVerificationMiddleware(get_response=lambda r: None)
            response = middleware(request)
            
            # Debe redirigir de inmediato al cambio forzado de contraseña
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/admin-panel/cambiar-contrasena/')
        finally:
            perfil_invitado.delete()
            inv.delete()

    def test_submit_forced_password_change_success(self):
        """Verifica que enviar el formulario con contraseña válida libere el acceso."""
        inv = InvitacionAdmin.objects.create(
            email=self.invite_email,
            nombre_completo='Pedro Perez',
            usuario_generado='admin_pedrop_8888',
            password_temporal_hash='pbkdf2_sha256$...',
            fecha_expiracion=django.utils.timezone.now() + django.utils.timezone.timedelta(days=7),
            estado='pendiente'
        )
        invited_uuid = str(uuid.uuid4())
        perfil_invitado = Perfil.objects.create(
            id=invited_uuid,
            nombre_completo='Pedro Perez',
            nombre_usuario='admin_pedrop_8888',
            rol='admin',
            rol_rbac=self.rol_admin,
            invitacion=inv,
            password_cambiada=False,
            esta_activo=True
        )

        # En SQLite, mock_request necesita tener el auth user registrado
        if getattr(settings, 'USE_SQLITE', False):
            with connection.cursor() as cursor:
                cursor.execute('INSERT OR IGNORE INTO "auth.users" (id, email) VALUES (%s, %s)', [invited_uuid, self.invite_email])

        try:
            # Petición POST con contraseñas correctas
            post_data = {
                'nueva_clave': 'MikiNuevaClave2026*',
                'confirmar_clave': 'MikiNuevaClave2026*'
            }
            request = self.get_mock_request(
                '/admin-panel/cambiar-contrasena/',
                method='POST',
                post_data=post_data,
                user_id=invited_uuid,
                role='admin'
            )
            
            response = cambiar_contrasena_forzado(request)
            
            # Debe redirigir al panel administrativo
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/admin-panel/')
            
            # Verificar cambios en base de datos
            perfil_invitado.refresh_from_db()
            self.assertTrue(perfil_invitado.password_cambiada)
            self.assertIsNotNone(perfil_invitado.fecha_primer_login)
            
            inv.refresh_from_db()
            self.assertEqual(inv.estado, 'aceptada')
            self.assertIsNotNone(inv.fecha_aceptacion)
        finally:
            perfil_invitado.delete()
            inv.delete()
            if getattr(settings, 'USE_SQLITE', False):
                with connection.cursor() as cursor:
                    cursor.execute('DELETE FROM "auth.users" WHERE id = %s', [invited_uuid])

    def test_revoke_invitation(self):
        """Verifica que revocar una invitación deshabilite el perfil del usuario."""
        inv = InvitacionAdmin.objects.create(
            email=self.invite_email,
            nombre_completo='Pedro Perez',
            usuario_generado='admin_pedrop_7777',
            password_temporal_hash='pbkdf2_sha256$...',
            fecha_expiracion=django.utils.timezone.now() + django.utils.timezone.timedelta(days=7),
            estado='pendiente'
        )
        invited_uuid = str(uuid.uuid4())
        perfil_invitado = Perfil.objects.create(
            id=invited_uuid,
            nombre_completo='Pedro Perez',
            nombre_usuario='admin_pedrop_7777',
            rol='admin',
            rol_rbac=self.rol_admin,
            invitacion=inv,
            password_cambiada=False,
            esta_activo=True
        )

        try:
            request = self.get_mock_request(
                f'/admin-panel/invitaciones/revocar/{inv.id}/',
                method='POST',
                user_id=self.superadmin_uuid,
                role='admin',
                permissions=['gestionar_usuarios']
            )
            
            response = revocar_invitacion_admin(request, inv.id)
            
            self.assertEqual(response.status_code, 302)
            
            # Validar cambios
            inv.refresh_from_db()
            self.assertEqual(inv.estado, 'revocada')
            
            perfil_invitado.refresh_from_db()
            self.assertFalse(perfil_invitado.esta_activo)
        finally:
            perfil_invitado.delete()
            inv.delete()


if __name__ == '__main__':
    unittest.main(verbosity=2)
