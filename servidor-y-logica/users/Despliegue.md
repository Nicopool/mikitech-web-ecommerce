Guía de Despliegue: Django + PostgreSQL + React (Vite)
Esta guía detalla el proceso para poner en marcha el proyecto MIKITECH, tanto en un servidor dedicado (VPS) como en entornos de nube (Railway y AWS/Azure).

---

## Preparación previa (Local y Producción)
Antes de desplegar en cualquier entorno, es indispensable compilar la aplicación React y preparar los archivos estáticos de Django:

1. **Construir el Frontend (React/Vite):**
   Ejecuta localmente (o permite que la canalización de CI/CD lo haga):
   ```bash
   npm run build
   ```
   Esto compilará los archivos de React sin hashes en la carpeta `dist/` (configurado en `vite.config.ts`), listos para ser consumidos por Django en producción.

2. **Generar Archivos Estáticos:**
   Con los archivos de React ya compilados en `dist/`, ejecuta:
   ```bash
   python manage.py collectstatic --noinput
   ```
   Esto copiará todos los archivos estáticos (incluyendo el bundle de React) en la carpeta `staticfiles/`, la cual será servida automáticamente y de forma optimizada por **WhiteNoise** en producción sin necesidad de Nginx.

---

## 1. Despliegue en Servidor Dedicado (VPS)
Sigue estos pasos en tu máquina virtual Ubuntu Server para configurar el entorno de producción:

### A. Instalar Python y Dependencias del Sistema
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv nodejs npm -y
```

### B. Clonar y Configurar el Entorno
```bash
cd /var/www
sudo git clone git@github.com:sena/proyecto-django.git MIKITECH-APP
cd MIKITECH-APP
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
```

### C. Configurar el Entorno de Producción y Migrar
1. Crea tu archivo `.env` en la raíz del servidor basándote en `.env.example` y define las variables en producción:
   - `DEBUG=False`
   - `ALLOWED_HOSTS=tudominio.com,ip-de-tu-servidor`
   - Configura las credenciales de Supabase o tu base de datos PostgreSQL de producción.
2. Ejecuta los comandos de preparación de base de datos y estáticos:
   ```bash
   npm run build
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```

### D. Configurar el Servidor de Aplicación (Gunicorn)
1. Inicia Gunicorn manualmente para probar:
   ```bash
   gunicorn mickytech.wsgi:application --bind 0.0.0.0:8000 --workers 3 --daemon
   ```
2. **Crear Servicio Systemd para mantener Gunicorn activo:**
   Crea el archivo del servicio:
   ```bash
   sudo nano /etc/systemd/system/gunicorn.service
   ```
   E ingresa el siguiente contenido adaptando las rutas:
   ```ini
   [Unit]
   Description=gunicorn daemon for MIKITECH-APP
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/var/www/MIKITECH-APP
   ExecStart=/var/www/MIKITECH-APP/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock mickytech.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```
   Inicia y habilita el servicio:
   ```bash
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn
   ```

---

## 2. Despliegue en Railway (Recomendado para aprendices SENA)
Railway realiza el despliegue automático conectándose a tu repositorio de GitHub. Gracias al `Procfile` y la configuración de `whitenoise` incluidos, el despliegue es sumamente simple:

1. **Instalar CLI de Railway (opcional para control local):**
   ```bash
   npm install -g @railway/cli
   ```
2. **Autenticar y asociar:**
   ```bash
   railway login
   railway init
   ```
3. **Servicio y Base de Datos:**
   - Si usas la base de datos externa (Supabase), añade las variables de entorno de tu `.env` directamente en la pestaña **Variables** del dashboard de tu proyecto en Railway.
   - De forma alternativa, puedes añadir un plugin de base de datos: `railway add --plugin postgresql`.
4. **Desplegar:**
   ```bash
   railway up
   ```
   *Nota: Railway detectará automáticamente el archivo [Procfile](file:///c:/Users/turca/Desktop/MIKITECH-APP/Procfile) y ejecutará `gunicorn mickytech.wsgi:application` para servir el sitio.*
5. **Ver Proyecto:**
   ```bash
   railway open
   ```

---

## 3. Despliegue en Nube con Prueba de 30 Días (Ej. Azure/AWS)
Para desplegar en plataformas que ofrecen 30 días de prueba gratuita, sigue estas instrucciones:

* **Registro:** Crea una cuenta en Azure o AWS y activa tu suscripción de prueba.
* **Crear Instancia (VM):** Crea una máquina virtual (Ubuntu Server). Asegúrate de abrir los puertos de entrada `80` (HTTP), `443` (HTTPS) y `8000` (Gunicorn/Django) en el Firewall / Grupo de Seguridad.
* **Conexión:** Accede a tu máquina virtual vía SSH:
  ```bash
  ssh usuario@ip-de-tu-servidor
  ```
* **Instalación:** Repite los pasos de la **Sección 1 (VPS)** dentro de tu máquina virtual.
* **Base de Datos:** En lugar de instalar PostgreSQL de forma local en la máquina virtual, utiliza el servicio de base de datos gestionada (como RDS en AWS o Azure Database for PostgreSQL) para una mayor estabilidad. Actualiza las variables de entorno de tu base de datos en el archivo `.env` del servidor.
* **Dominio:** Configura un registro de tipo **A** en tu proveedor de DNS apuntando a la dirección IP pública de tu máquina virtual.

> [!WARNING]
> **Nota de Antigravity:** Recuerda que al finalizar los 30 días de prueba gratuita de AWS/Azure, si no conviertes la cuenta a un plan de pago o detienes la instancia, el servicio podría ser suspendido y los datos eliminados. **Asegúrate de realizar respaldos regulares de tu base de datos de Supabase/RDS antes de finalizar el periodo.**
