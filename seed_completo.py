import os
import django
import random
import uuid
import time
from decimal import Decimal
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from products.models import Categoria, Producto
from users.models import Perfil
from interactions.models import Voto, Favorito, Reseña
from users.supabase_auth import registrar_usuario

print("Iniciando MIKITECH Data Reseeding Completo...")

# 1. Borrar Datos Anteriores Locales
print("Las tablas ya fueron truncadas por SQL.")

# 2. Generar 10 usuarios de prueba vía API
print("Generando 10 usuarios...")
usuarios_generados = []
for i in range(1, 11):
    email = f"user{i}_{uuid.uuid4().hex[:6]}@mikitech.test"
    username = f"gamer_{i}_{uuid.uuid4().hex[:4]}"
    # 2 admin, 8 clientes
    rol = 'admin' if i <= 2 else 'client'
    data, error = registrar_usuario(email, "SecurePass123*", f"User Test {i}", username, rol)
    if error:
        print(f"Error creando {email}: {error}")
    else:
        # El ID viene en data['user']['id']
        uid = data.get('user', {}).get('id')
        if uid:
            usuarios_generados.append({'id': uid, 'email': email, 'username': username})
    time.sleep(0.5)

print(f"Usuarios creados. Esperando 3s para que los triggers creen los perfiles...")
time.sleep(3)

perfiles = list(Perfil.objects.filter(id__in=[u['id'] for u in usuarios_generados]))
if not perfiles:
    # Fallback si el trigger falló, forzamos la creación
    print("El trigger no actuó. Creando perfiles manualmente...")
    for u in usuarios_generados:
        try:
            Perfil.objects.create(id=u['id'], nombre_completo=f"User Test {u['id']}", nombre_usuario=u['username'])
        except Exception:
            pass
    perfiles = list(Perfil.objects.filter(id__in=[u['id'] for u in usuarios_generados]))

# 3. Categorías
cat_names = ["Procesadores", "Tarjetas Gráficas", "Placas Base", "Memoria RAM", "Almacenamiento", 
             "Fuentes de Poder", "Gabinetes", "Refrigeración", "Monitores", "Periféricos"]
cat_objects = []
for cname in cat_names:
    cat = Categoria.objects.create(
        nombre=cname,
        enlace=slugify(cname),
        descripcion=f"Componentes para {cname.lower()}.",
        icono='hardware',
        url_imagen="https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea"
    )
    cat_objects.append(cat)

# 4. Productos (107)
brands = ['ASUS', 'MSI', 'Gigabyte', 'Corsair', 'AMD', 'Intel', 'NVIDIA', 'Western Digital']
prod_objects = []
for cat in cat_objects:
    num_to_create = 11 if cat.nombre == "Procesadores" else 10 # Para que sumen 107
    if cat.nombre in ["Tarjetas Gráficas", "Placas Base", "Memoria RAM", "Almacenamiento", "Fuentes de Poder", "Gabinetes"]:
        num_to_create = 11 # 11 * 7 = 77
    for i in range(num_to_create):
        brand = random.choice(brands)
        r = random.randint(100, 9999)
        name = f"{brand} {cat.nombre.split()[0]} Pro-{r}"
        
        prod = Producto.objects.create(
            categoria=cat,
            nombre=name,
            enlace=slugify(f"{name}-{uuid.uuid4().hex[:4]}"),
            descripcion="Componente de alto rendimiento.",
            precio=Decimal(random.uniform(50.0, 1500.0)).quantize(Decimal('0.01')),
            existencias=random.randint(5, 50),
            marca=brand,
            esta_activo=True,
            url_imagen_principal="https://images.unsplash.com/photo-1587202372634-32705e3bf49c"
        )
        prod_objects.append(prod)

# Para llegar a los 107 exactos si faltan
while len(prod_objects) < 107:
    cat = random.choice(cat_objects)
    brand = random.choice(brands)
    name = f"{brand} Extra-{random.randint(1000, 9999)}"
    prod = Producto.objects.create(
        categoria=cat,
        nombre=name,
        enlace=slugify(f"{name}-{uuid.uuid4().hex[:4]}"),
        precio=Decimal('99.99'),
        esta_activo=True
    )
    prod_objects.append(prod)

# 5. Favoritos (5 por usuario)
if perfiles and prod_objects:
    for perfil in perfiles:
        favoritos = random.sample(prod_objects, 5)
        for f in favoritos:
            try:
                Favorito.objects.create(usuario=perfil, producto=f)
            except Exception:
                pass

# 6. Votos (5 por producto)
# Como son 107 productos * 5 = 535 votos. Los repartimos entre los perfiles usando una función
import itertools
perfiles_cycle = itertools.cycle(perfiles)
if perfiles and prod_objects:
    for prod in prod_objects:
        # Cogemos 5 perfiles distintos aprox
        votantes = random.sample(perfiles, min(5, len(perfiles)))
        for votante in votantes:
            try:
                Voto.objects.create(usuario=votante, producto=prod)
            except Exception:
                pass

# 7. Reseñas (25 en total)
if perfiles and prod_objects:
    for _ in range(25):
        try:
            Reseña.objects.create(
                usuario=random.choice(perfiles),
                producto=random.choice(prod_objects),
                calificacion=random.randint(3, 5),
                comentario="¡Excelente producto! Muy recomendado para un buen build de PC.",
                esta_aprobada=True
            )
        except Exception:
            pass

print(f"✅ Seeding finalizado con éxito.")
print(f"- Perfiles: {len(perfiles)}")
print(f"- Productos: {len(prod_objects)}")
print(f"- Votos y Reseñas insertados correctamente.")
