import os
import sys
from pathlib import Path

# Agregar el directorio del backend al path de python
sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'servidor-y-logica'))

import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from users.supabase_auth import registrar_usuario, iniciar_sesion_usuario

email = f"debug_{uuid.uuid4().hex[:6]}@mikitech.test"
password = "SecurePassword123!"

print(f"--- DEBUG SUPABASE AUTH ---")
data, error = registrar_usuario(email, password, "Debug User", "debug_user")
print("Registro - Data:", data)
print("Registro - Error:", error)

data_l, error_l = iniciar_sesion_usuario(email, password)
print("Login - Data:", data_l)
print("Login - Error:", error_l)
