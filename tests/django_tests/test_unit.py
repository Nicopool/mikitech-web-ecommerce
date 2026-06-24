import os
import sys
from pathlib import Path
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta

# Agregar el directorio del backend al path de python
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'servidor-y-logica'))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

import unittest
from products.models import Producto

class TestProductoUnit(unittest.TestCase):
    def test_en_stock(self):
        """Prueba unitaria de la propiedad en_stock."""
        # Producto con stock
        prod_en_stock = Producto(nombre="Procesador Intel i9", existencias=5)
        self.assertTrue(prod_en_stock.en_stock)

        # Producto sin stock
        prod_sin_stock = Producto(nombre="Procesador Intel i7", existencias=0)
        self.assertFalse(prod_sin_stock.en_stock)

    def test_descuento_activo(self):
        """Prueba unitaria para verificar si el descuento está activo."""
        # Sin descuento
        prod = Producto(nombre="RAM DDR5", precio=100000, descuento_porcentaje=0)
        self.assertFalse(prod.descuento_activo)

        # Descuento activo sin fecha de expiración
        prod = Producto(nombre="RAM DDR5", precio=100000, descuento_porcentaje=10)
        self.assertTrue(prod.descuento_activo)

        # Descuento activo con expiración en el futuro
        prod = Producto(
            nombre="RAM DDR5", 
            precio=100000, 
            descuento_porcentaje=10, 
            descuento_expira_el=timezone.now() + timedelta(days=1)
        )
        self.assertTrue(prod.descuento_activo)

        # Descuento inactivo con expiración en el pasado
        prod = Producto(
            nombre="RAM DDR5", 
            precio=100000, 
            descuento_porcentaje=10, 
            descuento_expira_el=timezone.now() - timedelta(days=1)
        )
        self.assertFalse(prod.descuento_activo)

    def test_precio_con_descuento(self):
        """Prueba unitaria del cálculo del precio con descuento."""
        # Producto sin descuento
        prod = Producto(nombre="Monitor 4K", precio=Decimal('1000.00'), descuento_porcentaje=0)
        self.assertEqual(prod.precio_con_descuento, Decimal('1000.00'))

        # Producto con descuento del 20%
        prod = Producto(
            nombre="Monitor 4K", 
            precio=Decimal('1000.00'), 
            descuento_porcentaje=20,
            descuento_expira_el=timezone.now() + timedelta(days=1)
        )
        # 1000.00 * 0.8 = 800.00
        self.assertEqual(prod.precio_con_descuento, Decimal('800'))

if __name__ == "__main__":
    unittest.main(verbosity=2)
