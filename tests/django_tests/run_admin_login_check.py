import json
import urllib.request
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno y configurar Django
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'servidor-y-logica'))
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from users.models import Perfil

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_ANON_KEY')

def test_login(email, password):
    url = f"{SUPABASE_URL}/auth/v1/token?grant_type=password"
    headers = {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_KEY,
    }
    data = { 'email': email, 'password': password }
    
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            print(f"✅ ¡Login exitoso para {email}!")
            return True, None
    except Exception as e:
        print(f"❌ Falló el login para {email}: {e}")
        print("\n--- ADMINISTRADORES REGISTRADOS EN LA BASE DE DATOS ---")
        admins = Perfil.objects.filter(rol='admin')
        if admins.exists():
            for admin in admins:
                print(f"👤 Usuario: {admin.nombre_usuario} | Correo: {admin.email}")
            print("\n💡 Tip: Modifica la línea final de este archivo con uno de los correos de arriba y su contraseña correcta.")
        else:
            print("No se encontraron usuarios administradores en la base de datos.")
        print("------------------------------------------------------")
        return False, str(e)

if __name__ == "__main__":
    test_login("admin@mikitech.com", "AdminMiki2026*")

