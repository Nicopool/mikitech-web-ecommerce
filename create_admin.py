import json
import urllib.request
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(Path(__file__).resolve().parent / '.env')

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_ANON_KEY')

def register_admin(email, password, full_name, username):
    url = f"{SUPABASE_URL}/auth/v1/signup"
    headers = {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_KEY,
    }
    data = {
        'email': email,
        'password': password,
        'data': {
            'full_name': full_name,
            'username': username,
            'role': 'admin' # This might be ignored by Supabase if it's not configured to trust it, but we'll fix it in SQL later
        }
    }
    
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            print(f"User created: {res.get('id')}")
            return res.get('id')
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    register_admin("admin@mikitech.com", "AdminMiki2026*", "Administrador Principal", "mikiadmin")
