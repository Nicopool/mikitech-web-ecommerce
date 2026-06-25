import os
import sys
from pathlib import Path

# Agregar el directorio del backend al path de python
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Reconfigurar salida para evitar errores Unicode en consolas Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from users.supabase_auth import registrar_usuario, registrar_usuario_sql, iniciar_sesion_usuario, enviar_recuperacion_contraseña

print("--- TESTING SUPABASE AUTH CONNECTIONS ---")

email = "testuser_12345@mikitech.test"
password = "SecurePassword123!"

# 1. Register User
print(f"1. Registrando usuario: {email}")
data, error = registrar_usuario(email, password, "Test User", "testuser_12345")
if error:
    print(f"[WARNING] Error en registro inicial: {error}")
    if "confirmation email" in error.lower():
        print("[!] Reintentando registro directo mediante SQL (Bypass de confirmación SMTP)...")
        data, error = registrar_usuario_sql(email, password, "Test User", "testuser_12345")
        if error:
            print(f"[ERROR] Falló el fallback de registro SQL: {error}")
        else:
            print("[OK] Registro completado exitosamente vía SQL.")
    else:
        print(f"[ERROR] Error en registro: {error}")
else:
    print("[OK] Registro completado.")

# 2. Login User
print(f"2. Iniciando sesión de: {email}")
data_login, error_login = iniciar_sesion_usuario(email, password)
if error_login:
    # Si requiere confirmación de email (Supabase por defecto la tiene activada)
    print(f"[WARNING] Error en inicio de sesión (puede requerir conf de email): {error_login}")
else:
    print("[OK] Autenticación exitosa. Token obtenido.")

# 3. Recuperar contraseña
print(f"3. Probando recuperación de contraseña a: {email}")
data_rec, error_rec = enviar_recuperacion_contraseña(email)
if error_rec:
    print(f"[ERROR] Error en recuperación: {error_rec}")
else:
    print("[OK] Envío de recuperación exitoso.")

print("-----------------------------------------")
