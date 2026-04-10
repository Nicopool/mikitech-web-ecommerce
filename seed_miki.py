import os
import django
import random
from decimal import Decimal
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

# Se asume que el script correrá con python seed_miki.py
from products.models import Category, Product

# Se asume que el script correrá en el contexto de shell de manage.py o con django setup.
from products.models import Category, Product

print("Iniciando MIKITECH Data Reseeding Categórico...")

# 1. Borrar Catálogos Actuales
print("Borrando productos y categorías anteriores...")
Product.objects.all().delete()
Category.objects.all().delete()

# 2. 10 Categorías MIKITECH Oficiales
cat_names = [
    "Procesadores",
    "Tarjetas Gráficas",
    "Placas Base",
    "Memoria RAM",
    "Almacenamiento",
    "Fuentes de Poder",
    "Gabinetes",
    "Refrigeración",
    "Monitores",
    "Periféricos"
]

cat_objects = []
for idx, cname in enumerate(cat_names):
    cat = Category.objects.create(
        name=cname,
        slug=slugify(cname),
        description=f"Hardware especializado en {cname.lower()}.",
        icon='hardware'
    )
    cat_objects.append(cat)
print("✅ Creadas 10 Categorías MIKITECH.")

# 3. Datos mock para productos (para llegar a 107)
brands = ['ASUS', 'MSI', 'Gigabyte', 'Corsair', 'AMD', 'Intel', 'NVIDIA', 'Western Digital', 'Samsung', 'Kingston']
adjectives = ['Pro', 'Elite', 'Gaming', 'X-Treme', 'Quantum', 'Max', 'Ultra', 'Evo', 'Suprema', 'Titan']

product_list = []
target_products = 107

products_per_category = target_products // len(cat_objects)
remainder = target_products % len(cat_objects)

def generate_product_name(cat_name):
    brand = random.choice(brands)
    adj = random.choice(adjectives)
    model_num = random.randint(1000, 9999)
    if 'Procesador' in cat_name:
        return f"{brand} {adj} Core i{random.choice([5,7,9])}-{model_num}X"
    if 'Gráfica' in cat_name:
        return f"{brand} RTX {model_num} {adj}"
    if 'Almacenamiento' in cat_name:
        return f"{brand} SSD {random.choice(['1TB', '2TB', '500GB'])} {adj} NVMe"
    if 'Memoria' in cat_name:
        return f"{brand} {adj} DDR5 {random.choice(['16GB', '32GB', '64GB'])} {model_num}MHz"
    return f"{brand} {cat_name.split()[0]} {adj} {model_num}"

print(f"Generando {target_products} productos distribuidos en las 10 categorías...")

created_count = 0
for i, cat in enumerate(cat_objects):
    num_to_create = products_per_category + (1 if i < remainder else 0)
    
    for _ in range(num_to_create):
        name = generate_product_name(cat.name)
        price = Decimal(random.uniform(50.0, 1500.0)).quantize(Decimal('0.01'))
        stock = random.randint(0, 100)
        is_featured = random.choice([True, False, False, False]) # 25% chance of featured
        
        # Add realistic random images depending on category, or use the general Unsplash hardware pool
        images = [
            "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&q=80&w=600",
            "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&q=80&w=600",
            "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&q=80&w=600",
            "https://images.unsplash.com/photo-1624704795325-1ff2d3d950de?auto=format&fit=crop&q=80&w=600",
            "https://images.unsplash.com/photo-1555680202-c86f0e12f086?auto=format&fit=crop&q=80&w=600"
        ]
        
        brand_name = random.choice(brands)
        Product.objects.create(
            category=cat,
            name=name,
            slug=slugify(f"{name} {random.randint(1,9999)}"),
            description=f"Componente de nivel empresarial para {cat.name.lower()}. Construido con los mejores materiales.",
            price=price,
            stock=stock,
            brand=brand_name,
            model=name.split()[-1],
            is_active=True,
            is_featured=is_featured,
            main_image_url=random.choice(images),
            specifications={'brand': brand_name, 'warranty': '2 Años', 'category': cat.name}
        )
        created_count += 1

print(f"✅ Seeding Finalizado. Se crearon {created_count} productos en 10 categorías.")
