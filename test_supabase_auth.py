import os

import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')
django.setup()

from users.supabase_auth import registrar_usuario, iniciar_sesion_usuario, enviar_recuperacion_contraseña

print("--- TESTING SUPABASE AUTH CONNECTIONS ---")

email = "testuser_12345@mikitech.test"
password = "SecurePassword123!"

# 1. Regsiter User
print(f"1. Registrando usuario: {email}")
data, error = registrar_usuario(email, password, "Test User", "testuser_12345")
if error:
    print(f"❌ Error en registro: {error}")
else:
    print("✅ Registro completado.")

# 2. Login User
print(f"2. Iniciando sesión de: {email}")
data_login, error_login = iniciar_sesion_usuario(email, password)
if error_login:
    # Si requiere confirmación de email (Supabase por defecto la tiene activada)
    print(f"⚠️ Error en inicio de sesión (puede requerir conf de email): {error_login}")
else:
    print("✅ Autenticación exitosa. Token obtenido.")

# 3. Recuperar contraseña
print(f"3. Probando recuperación de contraseña a: {email}")
data_rec, error_rec = enviar_recuperacion_contraseña(email)
if error_rec:
    print(f"❌ Error en recuperación: {error_rec}")
else:
    print("✅ Envío de recuperación exitoso.")

print("-----------------------------------------")
