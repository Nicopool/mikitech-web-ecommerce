from users.models import Perfil
from products.models import Producto
from interactions.models import Pedido
import random
from decimal import Decimal

u = Perfil.objects.get(nombre_usuario='realuser999')
ests = ['Entregado', 'En camino', 'Pendiente', 'Procesando']
for _ in range(10):
    Pedido.objects.create(
        usuario=u,
        estado=random.choice(ests),
        monto_total=Decimal(random.randint(500000, 5000000)),
        direccion_envio='Calle Falsa 123'
    )
print('Seed complete.')
