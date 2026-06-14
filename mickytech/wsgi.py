"""
WSGI config for mickytech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mickytech.settings')

application = get_wsgi_application()

# Envolver la aplicación con WhiteNoise y servir desde las carpetas origen directamente
# Esto evita depender enteramente de collectstatic en entornos efímeros de Railway
application = WhiteNoise(application, root=settings.STATIC_ROOT)

# Registrar carpeta static
static_dir = os.path.join(settings.BASE_DIR, 'static')
if os.path.exists(static_dir):
    application.add_files(static_dir, prefix='static/')

# Registrar carpeta dist (Vite build)
dist_dir = os.path.join(settings.BASE_DIR, 'dist')
if os.path.exists(dist_dir):
    application.add_files(dist_dir, prefix='static/')


