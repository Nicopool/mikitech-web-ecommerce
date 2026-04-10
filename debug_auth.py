import os
import django
import sys
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
