import os
import sys
import json
from pathlib import Path
from django.utils.text import slugify

# Add workspace root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
import django
django.setup()

from products.models import Categoria, Producto

def seed():
    # Load JSON file
    json_path = Path(__file__).resolve().parent.parent / 'productos_carga_masiva.json'
    if not json_path.exists():
        print(f"Error: {json_path} does not exist.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Loading {len(data)} products from JSON...")
    
    categories_created = 0
    products_created = 0

    for item in data:
        cat_name = item.get('CATEGORIA', 'General')
        cat_slug = slugify(cat_name)
        
        # Get or create Category
        categoria, created = Categoria.objects.get_or_create(
            enlace=cat_slug,
            defaults={
                'nombre': cat_name,
                'descripcion': f'Categoría {cat_name}'
            }
        )
        if created:
            categories_created += 1

        # Product details
        prod_name = item.get('NOMBRE')
        prod_slug = slugify(prod_name)
        
        # Ensure slug is unique by appending suffix if needed
        base_slug = prod_slug
        counter = 1
        while Producto.objects.filter(enlace=prod_slug).exists():
            prod_slug = f"{base_slug}-{counter}"
            counter += 1

        # Randomize discount to test discounts
        import random
        has_discount = random.random() < 0.35  # 35% chance of discount
        discount_percentage = random.choice([10, 15, 20, 25, 30]) if has_discount else 0

        # Create Product
        producto = Producto.objects.create(
            categoria=categoria,
            nombre=prod_name,
            enlace=prod_slug,
            descripcion=item.get('DESCRIPCION', ''),
            precio=item.get('PRECIO', 0),
            existencias=item.get('STOCK', 0),
            marca=item.get('MARCA', ''),
            url_imagen_principal=item.get('URL_IMAGEN') or "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3",
            descuento_porcentaje=discount_percentage,
            es_destacado=random.random() < 0.25, # 25% chance of being featured
            esta_activo=True
        )
        products_created += 1

    print(f"[SUCCESS] Created {categories_created} categories and {products_created} products!")

if __name__ == '__main__':
    seed()
