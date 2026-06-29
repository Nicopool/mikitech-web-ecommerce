"""PRUEBAS UNITARIAS - Modelos de Productos"""

from decimal import Decimal
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from products.models import Producto, Categoria, ImagenProducto


class TestProductoUnit(TestCase):
    """Pruebas unitarias para el modelo Producto (propiedades y métodos)."""

    def test_en_stock_con_existencias_positivas(self):
        prod = Producto(existencias=5)
        self.assertTrue(prod.en_stock)

    def test_en_stock_con_existencias_cero(self):
        prod = Producto(existencias=0)
        self.assertFalse(prod.en_stock)

    def test_en_stock_con_existencias_negativas(self):
        prod = Producto(existencias=-1)
        self.assertFalse(prod.en_stock)

    def test_descuento_inactivo_sin_porcentaje(self):
        prod = Producto(descuento_porcentaje=0)
        self.assertFalse(prod.descuento_activo)

    def test_descuento_inactivo_con_porcentaje_negativo(self):
        prod = Producto(descuento_porcentaje=-5)
        self.assertFalse(prod.descuento_activo)

    def test_descuento_activo_sin_expiracion(self):
        prod = Producto(descuento_porcentaje=10)
        self.assertTrue(prod.descuento_activo)

    def test_descuento_activo_con_expiracion_futura(self):
        prod = Producto(
            descuento_porcentaje=10,
            descuento_expira_el=timezone.now() + timedelta(days=1)
        )
        self.assertTrue(prod.descuento_activo)

    def test_descuento_inactivo_con_expiracion_pasada(self):
        prod = Producto(
            descuento_porcentaje=10,
            descuento_expira_el=timezone.now() - timedelta(days=1)
        )
        self.assertFalse(prod.descuento_activo)

    def test_precio_sin_descuento_igual_al_original(self):
        prod = Producto(precio=Decimal('1000.00'), descuento_porcentaje=0)
        self.assertEqual(prod.precio_con_descuento, Decimal('1000.00'))

    def test_precio_con_descuento_20_porciento(self):
        prod = Producto(
            precio=Decimal('1000.00'),
            descuento_porcentaje=20,
            descuento_expira_el=timezone.now() + timedelta(days=1)
        )
        self.assertEqual(prod.precio_con_descuento, Decimal('800'))

    def test_precio_con_descuento_50_porciento(self):
        prod = Producto(
            precio=Decimal('250000.00'),
            descuento_porcentaje=50,
            descuento_expira_el=timezone.now() + timedelta(days=1)
        )
        self.assertEqual(prod.precio_con_descuento, Decimal('125000'))

    def test_precio_con_descuento_expirado_igual_al_original(self):
        prod = Producto(
            precio=Decimal('500.00'),
            descuento_porcentaje=30,
            descuento_expira_el=timezone.now() - timedelta(days=1)
        )
        self.assertEqual(prod.precio_con_descuento, Decimal('500.00'))

    def test_calificacion_promedio_sin_resenas(self):
        prod = Producto()
        self.assertEqual(prod.calificacion_promedio, 0)

    def test_str_retorna_nombre(self):
        prod = Producto(nombre='Procesador AMD Ryzen 9')
        self.assertEqual(str(prod), 'Procesador AMD Ryzen 9')


class TestCategoriaUnit(TestCase):
    """Pruebas unitarias para el modelo Categoria."""

    def test_str_retorna_nombre(self):
        cat = Categoria(nombre='Procesadores')
        self.assertEqual(str(cat), 'Procesadores')

    def test_crear_categoria_con_datos_minimos(self):
        cat = Categoria.objects.create(
            nombre='Tarjetas Gráficas',
            enlace='tarjetas-graficas'
        )
        self.assertEqual(cat.nombre, 'Tarjetas Gráficas')
        self.assertEqual(cat.enlace, 'tarjetas-graficas')
        self.assertIsNotNone(cat.id)


class TestImagenProductoUnit(TestCase):
    """Pruebas unitarias para el modelo ImagenProducto."""

    def test_str_retorna_nombre_producto(self):
        prod = Producto(nombre='Monitor 4K')
        img = ImagenProducto(producto=prod, url_imagen='http://ejemplo.com/img.jpg')
        self.assertEqual(str(img), 'Imagen de Monitor 4K')
