import json
import urllib.request
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(Path(__file__).resolve().parent / '.env')

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
            print("Login success!")
            return True, None
    except Exception as e:
        print(f"Login failed: {e}")
        return False, str(e)

if __name__ == "__main__":
    test_login("admin@mikitech.com", "AdminMiki2026*")
