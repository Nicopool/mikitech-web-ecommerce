import os
import sys
from pathlib import Path

# Agregar el directorio del backend al path de python
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'servidor-y-logica'))

import django
import random
import itertools

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from products.models import Producto
from users.models import Perfil
from interactions.models import Voto, Favorito, Reseña

print("Iniciando generación de interacciones...")

perfiles = list(Perfil.objects.all())[:10]
prod_objects = list(Producto.objects.all())

print(f"Perfiles encontrados: {len(perfiles)}")
print(f"Productos encontrados: {len(prod_objects)}")

if perfiles and prod_objects:
    # 5. Favoritos (5 por usuario)
    print("Creando favoritos...")
    for perfil in perfiles:
        favoritos = random.sample(prod_objects, 5)
        for f in favoritos:
            try:
                Favorito.objects.create(usuario=perfil, producto=f)
            except Exception:
                pass

    # 6. Votos (5 por producto)
    print("Creando votos...")
    for prod in prod_objects:
        votantes = random.sample(perfiles, min(5, len(perfiles)))
        for votante in votantes:
            try:
                Voto.objects.create(usuario=votante, producto=prod)
            except Exception:
                pass

    # 7. Reseñas (25 en total)
    print("Creando reseñas...")
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

print("✅ Generación de interacciones finalizada.")
