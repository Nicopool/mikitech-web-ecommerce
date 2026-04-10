import os
import django
import random
import uuid
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from users.models import Perfil
from products.models import Producto
from interactions.models import Pedido, DetallePedido

def create_test_orders():
    # User to assign orders to
    user = Perfil.objects.filter(nombre_usuario='realuser999').first()
    if not user:
        print("User realuser999 not found.")
        return

    # Products to use for details
    products = list(Producto.objects.all()[:10])
    if not products:
        print("No products found to create order details.")
        return

    estados = ['Entregado', 'En camino', 'Pendiente', 'Procesando']
    direcciones = [
        'Calle 10 # 45-20, Bogotá',
        'Carrera 7 # 100-30, Medellín',
        'Avenida Siempre Viva 742, Cali',
        'C.C. Andino Local 102, Bogotá'
    ]

    print(f"Creating 10 orders for {user.nombre_mostrado}...")

    for i in range(10):
        # Create Pedido
        monto = Decimal(random.randint(500000, 5000000))
        pedido = Pedido.objects.create(
            usuario=user,
            estado=random.choice(estados),
            monto_total=monto,
            direccion_envio=random.choice(direcciones),
            notas=f"Pedido de prueba #{i+1} generado para validación de dashboard."
        )

        # Add 1-3 random products to the order
        num_items = random.randint(1, 3)
        for _ in range(num_items):
            prod = random.choice(products)
            cant = random.randint(1, 2)
            DetallePedido.objects.create(
                pedido=pedido,
                producto=prod,
                cantidad=cant,
                precio_unitario=prod.precio or Decimal('150000')
            )

    print("Success: 10 test orders created.")

if __name__ == "__main__":
    create_test_orders()
