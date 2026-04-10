from users.models import Perfil
from interactions.models import Pedido
u = Perfil.objects.filter(nombre_completo__icontains='Nicolas').first() or Perfil.objects.filter(nombre_usuario__icontains='Nicolas').first()
if u:
    print(f'User found: {u.nombre_mostrado}')
    print(f'Orders count: {Pedido.objects.filter(usuario=u).count()}')
else:
    print('User Nicolas not found.')
