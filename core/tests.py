"""PRUEBAS DE INTEGRACIÓN - API + BD + Autenticación"""

import uuid
from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.contrib.sessions.backends.signed_cookies import SessionStore
from products.models import Producto, Categoria
from users.models import Perfil
from interactions.models import Pedido, DetallePedido


class TestPublicEndpoints(TestCase):
    """Integración: endpoints públicos funcionando con la BD."""

    def setUp(self):
        self.client = Client()
        self.categoria = Categoria.objects.create(
            nombre='Procesadores',
            enlace='procesadores'
        )
        self.producto = Producto.objects.create(
            nombre='AMD Ryzen 9 7950X',
            enlace='amd-ryzen-9-7950x',
            precio=Decimal('2500000.00'),
            existencias=10,
            categoria=self.categoria,
            esta_activo=True
        )

    def test_ping_endpoint_retorna_json_ok(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok', 'msg': 'pong'})

    def test_home_page_carga_correctamente(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 200:
            self.assertIn(b'MIKITECH', response.content)

    def test_lista_productos_muestra_producto_activo(self):
        response = self.client.get('/productos/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AMD Ryzen 9 7950X', response.content)

    def test_detalle_producto_por_slug(self):
        response = self.client.get(f'/productos/{self.producto.enlace}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AMD Ryzen 9 7950X', response.content)

    def test_detalle_producto_404_si_slug_invalido(self):
        response = self.client.get('/productos/slug-inexistente/')
        self.assertEqual(response.status_code, 404)

    def test_buscar_producto_por_nombre(self):
        response = self.client.get('/buscar/?q=Ryzen')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AMD Ryzen 9 7950X', response.content)

    def test_buscar_sin_resultados(self):
        response = self.client.get('/buscar/?q=zzzzznoexiste')
        self.assertEqual(response.status_code, 200)

    def test_carrito_vacio_devuelve_200(self):
        response = self.client.get('/carrito/')
        self.assertEqual(response.status_code, 200)

    def test_api_cart_status_sin_sesion(self):
        response = self.client.get('/api/cart-status/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('total_articulos', data)
        self.assertIn('total_bruto', data)
        self.assertIn('total_formateado', data)
        self.assertEqual(data['total_articulos'], 0)


class TestAuthFlowIntegration(TestCase):
    """Integración: flujo completo de autenticación."""

    def setUp(self):
        self.client = Client()

    def test_registro_usuario_nuevo(self):
        uid = uuid.uuid4().hex[:8]
        data = {
            'nombre_completo': 'Test Usuario',
            'nombre_usuario': f'testuser_{uid}',
            'correo': f'test_{uid}@gmail.com',
            'clave': 'Password123!',
            'clave2': 'Password123!',
            'terminos': 'on'
        }
        response = self.client.post('/cuenta/registro/', data)
        # El registro renderiza la página de login con mensaje de éxito (200)
        # o redirige si la autenticación local funciona (302)
        self.assertIn(response.status_code, [200, 302])

    def test_registro_contrasenas_no_coinciden(self):
        uid = uuid.uuid4().hex[:8]
        data = {
            'nombre_completo': 'Test Usuario',
            'nombre_usuario': f'testuser_{uid}',
            'correo': f'test_{uid}@gmail.com',
            'clave': 'Password123!',
            'clave2': 'Password456!',
            'terminos': 'on'
        }
        response = self.client.post('/cuenta/registro/', data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'coinciden', response.content)

    def test_login_redirige_a_perfil(self):
        uid = uuid.uuid4().hex[:8]
        username = f'testuser_{uid}'
        email = f'test_{uid}@gmail.com'
        Perfil.objects.create(
            id=str(uuid.uuid4()),
            nombre_completo='Test User',
            nombre_usuario=username,
            email=email,
            rol='client',
            esta_activo=True
        )
        response = self.client.post('/cuenta/ingreso/', {
            'correo': email,
            'clave': 'Password123!'
        })
        self.assertIn(response.status_code, [200, 302])

    def test_perfil_requiere_autenticacion(self):
        response = self.client.get('/cuenta/perfil/')
        self.assertEqual(response.status_code, 302)


class TestCartFlowIntegration(TestCase):
    """Integración: flujo completo del carrito de compras."""

    def setUp(self):
        self.client = Client()
        self.categoria = Categoria.objects.create(
            nombre='Componentes',
            enlace='componentes'
        )
        self.producto = Producto.objects.create(
            nombre='SSD NVMe 1TB',
            enlace='ssd-nvme-1tb',
            precio=Decimal('450000.00'),
            existencias=10,
            categoria=self.categoria,
            esta_activo=True
        )

    def test_agregar_producto_al_carrito(self):
        response = self.client.post(
            f'/carrito/agregar/{self.producto.id}/',
            {'cantidad': 1}
        )
        self.assertIn(response.status_code, [200, 302])

    def test_ver_carrito_con_producto_agregado(self):
        session = self.client.session
        session['carrito'] = {str(self.producto.id): 2}
        session.save()
        response = self.client.get('/carrito/')
        self.assertEqual(response.status_code, 200)

    def test_checkout_redirige_si_no_autenticado(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)


class TestAdminPanelIntegration(TestCase):
    """Integración: panel de administración."""

    def setUp(self):
        self.client = Client()
        self.admin = Perfil.objects.create(
            id=str(uuid.uuid4()),
            nombre_completo='Admin Test',
            nombre_usuario=f'admin_test_{uuid.uuid4().hex[:6]}',
            rol='admin',
            esta_activo=True
        )
        self.categoria = Categoria.objects.create(
            nombre='Gabinetes',
            enlace='gabinetes'
        )
        self.producto = Producto.objects.create(
            nombre='Gabinete NZXT H510',
            enlace='gabinete-nzxt-h510',
            precio=Decimal('350000.00'),
            existencias=5,
            categoria=self.categoria,
            esta_activo=True
        )

    def test_admin_login_redirige(self):
        response = self.client.post('/admin-panel/login/', {
            'codigo_acceso': 'test',
            'correo': 'admin@test.com',
            'clave': 'test123'
        })
        self.assertIn(response.status_code, [200, 302])

    def test_admin_panel_bloqueado_sin_sesion(self):
        response = self.client.get('/admin-panel/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin-panel/login/', response.url)

    def test_admin_productos_listado(self):
        response = self.client.get('/admin-panel/productos/')
        self.assertEqual(response.status_code, 302)

    def test_crear_producto_get_devuelve_formulario(self):
        session = SessionStore()
        session['usuario_id'] = self.admin.id
        session['rol_usuario'] = 'admin'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key
        response = self.client.get('/admin-panel/productos/crear/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Producto', response.content)

    def test_editar_producto_get_devuelve_formulario(self):
        session = SessionStore()
        session['usuario_id'] = self.admin.id
        session['rol_usuario'] = 'admin'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key
        response = self.client.get(
            f'/admin-panel/productos/editar/{self.producto.id}/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'NZXT', response.content)


    def test_editar_producto_post_nombre_vacio_devuelve_error(self):
        session = SessionStore()
        session['usuario_id'] = self.admin.id
        session['rol_usuario'] = 'admin'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key
        response = self.client.post(
            f'/admin-panel/productos/editar/{self.producto.id}/',
            {'nombre': '', 'precio': '1000', 'existencias': '5'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'obligatorio', response.content)

    def test_editar_producto_post_precio_invalido_devuelve_error(self):
        session = SessionStore()
        session['usuario_id'] = self.admin.id
        session['rol_usuario'] = 'admin'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key
        response = self.client.post(
            f'/admin-panel/productos/editar/{self.producto.id}/',
            {'nombre': 'Producto Test', 'precio': 'abc', 'existencias': '5'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'precio debe ser', response.content)

    def test_editar_producto_post_existencias_invalidas_devuelve_error(self):
        session = SessionStore()
        session['usuario_id'] = self.admin.id
        session['rol_usuario'] = 'admin'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key
        response = self.client.post(
            f'/admin-panel/productos/editar/{self.producto.id}/',
            {'nombre': 'Producto Test', 'precio': '1000', 'existencias': 'no-numero'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'entero', response.content)

    def test_editar_producto_post_valido_redirige(self):
        session = SessionStore()
        session['usuario_id'] = self.admin.id
        session['rol_usuario'] = 'admin'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key
        response = self.client.post(
            f'/admin-panel/productos/editar/{self.producto.id}/',
            {'nombre': 'Gabinete Editado', 'precio': '400000', 'existencias': '10'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/admin-panel/productos/')

    def test_crear_producto_post_nombre_vacio_devuelve_error(self):
        session = SessionStore()
        session['usuario_id'] = self.admin.id
        session['rol_usuario'] = 'admin'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key
        response = self.client.post(
            '/admin-panel/productos/crear/',
            {'nombre': '', 'precio': '1000', 'existencias': '5', 'id_categoria': self.categoria.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'obligatorio', response.content)


class TestInteractionsIntegration(TestCase):
    """Integración: votos, reseñas y favoritos."""

    def setUp(self):
        self.client = Client()
        self.usuario = Perfil.objects.create(
            id=str(uuid.uuid4()),
            nombre_completo='Test User',
            nombre_usuario=f'user_{uuid.uuid4().hex[:6]}',
            rol='client',
            esta_activo=True
        )
        self.categoria = Categoria.objects.create(
            nombre='Teclados',
            enlace='teclados'
        )
        self.producto = Producto.objects.create(
            nombre='Teclado Mecánico RGB',
            enlace='teclado-mecanico-rgb',
            precio=Decimal('200000.00'),
            existencias=15,
            categoria=self.categoria,
            esta_activo=True
        )

    def test_voto_requiere_autenticacion(self):
        response = self.client.post(
            f'/interacciones/votar/{self.producto.id}/'
        )
        # Las vistas de interacción devuelven 401 JSON si no hay sesión
        self.assertEqual(response.status_code, 401)

    def test_resena_requiere_autenticacion(self):
        response = self.client.post(
            f'/interacciones/reseñar/{self.producto.id}/',
            {'comentario': 'Excelente producto', 'calificacion': 5}
        )
        self.assertEqual(response.status_code, 302)

    def test_favorito_requiere_autenticacion(self):
        response = self.client.post(
            f'/interacciones/favorito/{self.producto.id}/'
        )
        self.assertEqual(response.status_code, 401)
