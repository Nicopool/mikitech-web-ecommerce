"""
WSGI config for mickytech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')

application = get_wsgi_application()

# Ejecutar collectstatic al iniciar si la carpeta de estáticos no existe o está vacía
from django.conf import settings
if not os.path.exists(settings.STATIC_ROOT) or not os.listdir(settings.STATIC_ROOT):
    from django.core.management import call_command
    try:
        print("Iniciando collectstatic automático...")
        call_command('collectstatic', interactive=False)
    except Exception as e:
        print(f"Error ejecutando collectstatic: {e}")

