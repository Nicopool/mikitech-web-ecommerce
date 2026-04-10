from users.models import Perfil
from products.models import Producto
from interactions.models import Pedido
import random
from decimal import Decimal
import datetime

# Find profile by different possible identifying strings
profiles = Perfil.objects.all()
target = None
for p in profiles:
    if any(s in str(p.nombre_mostrado).lower() or s in str(p.nombre_usuario).lower() for s in ['nicolas', 'turca']):
        target = p
        break

if not target:
    print("Could not find profile for 'turcanicolas1@gmail.com'.")
else:
    print(f"Adding 20 test orders to: {target.nombre_mostrado} (@{target.nombre_usuario})")
    ests = ['Entregado', 'En camino', 'Pendiente', 'Procesando']
    
    for _ in range(20):
        monto = Decimal(random.randint(450000, 10000000))
        Pedido.objects.create(
            usuario=target,
            estado=random.choice(ests),
            monto_total=monto,
            direccion_envio='Carrera 15 # 82-45, Bogotá'
        )
    print("Sucess: 20 test orders added.")
