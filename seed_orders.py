import os
import django
import random
import uuid
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from django.db import connection
from users.models import Profile

def seed_orders(email):
    try:
        user = Profile.objects.get(email=email)
    except Profile.DoesNotExist:
        print(f"User with email {email} not found.")
        user = Profile.objects.filter(role='client').first()
        if not user:
            print("No clients found.")
            return

    # Let's see what products exist
    from products.models import Product
    products = list(Product.objects.all()[:20])
    if not products:
        print("No products found to create orders.")
        return

    statuses = ['pending', 'shipped', 'delivered', 'cancelled']
    
    with connection.cursor() as cursor:
        for i in range(10):
            # Pick 1-3 random products
            order_prods = random.sample(products, k=random.randint(1, 3))
            
            total = 0
            order_id = str(uuid.uuid4())
            status = random.choice(statuses)
            tracking = f"TRK-{uuid.uuid4().hex[:8].upper()}"
            created_at = datetime.now() - timedelta(days=random.randint(1, 30))
            
            # Insert Order
            cursor.execute("""
                INSERT INTO orders (id, user_id, status, shipping_address, city, tracking_number, total_amount, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, [
                order_id, str(user.id), status, "Calle Verdadera 123", "Bogotá", tracking, 0, created_at, created_at
            ])
            
            for p in order_prods:
                qty = random.randint(1, 2)
                price = p.price
                total += price * qty
                
                item_id = str(uuid.uuid4())
                cursor.execute("""
                    INSERT INTO order_items (id, order_id, product_id, quantity, price_at_purchase, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, [
                    item_id, order_id, str(p.id), qty, price, created_at
                ])
                
            # Update order total
            cursor.execute("UPDATE orders SET total_amount = %s WHERE id = %s", [total, order_id])
            
        connection.commit()
    print(f"Successfully created 10 mock orders for {user.email}.")

if __name__ == "__main__":
    seed_orders("turcanicolas1@gmail.com")
