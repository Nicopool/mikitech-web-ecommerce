# Guía de Pruebas de Carga con Locust para MIKITECH

Esta guía describe cómo instalar, configurar y ejecutar pruebas de carga utilizando **Locust** en lugar de k6 para evaluar el rendimiento de la aplicación Django.

---

## 📋 1. ¿Qué es Locust?
Locust es una herramienta de prueba de carga basada en Python. A diferencia de k6 (que usa JavaScript y se ejecuta en consola), Locust te permite definir el comportamiento de los usuarios en código de Python puro y proporciona una **interfaz gráfica web interactiva** a la que puedes acceder desde tu navegador.

---

## 🚀 2. Instalación

Para instalar Locust en tu entorno virtual de Python, ejecuta:

```bash
pip install locust
```

*Nota: También se ha agregado al archivo `requirements.txt` de la aplicación.*

---

## 🛠️ 3. Ejecución del Test

1. Asegúrate de tener levantado el servidor de producción local con **Waitress**:
   ```bash
   waitress-serve --port=8000 --threads=20 mickytech.wsgi:application
   ```

2. Abre otra terminal, posiciónate en la raíz del proyecto y arranca Locust apuntando al archivo del test:
   ```bash
   locust -f tests/load/locustfile.py
   ```

3. Verás una salida en consola similar a:
   ```text
   [INFO] Starting web interface at http://0.0.0.0:8089
   ```

---

## 💻 4. Configuración en la Interfaz Web (Dashboard)

Abre tu navegador e ingresa a **`http://localhost:8089`**. Verás el panel de control de Locust con tres campos a rellenar:

1. **Number of users (Usuarios totales):** La cantidad máxima de usuarios virtuales concurrentes que quieres simular (ej: `50`).
2. **Spawn rate (Tasa de subida):** Cuántos usuarios nuevos se crean por segundo (ej: `5` para crear 5 usuarios cada segundo hasta llegar a 50).
3. **Host:** La dirección base de tu servidor local:
   ```text
   http://localhost:8000
   ```

Haz clic en **"Start swarming"** para comenzar la prueba.

---

## 📊 5. Visualización de Resultados
En la interfaz web de Locust tienes 4 pestañas clave:

*   **Statistics:** Muestra la cantidad de peticiones enviadas por cada endpoint (`/`, `/productos/`, `/carrito/`), tasa de fallos, y tiempos de respuesta (promedio, mediana, p95).
*   **Charts:** Gráficos visuales en tiempo real del número de usuarios, peticiones por segundo (RPS) y tiempos de respuesta.
*   **Failures:** Lista de errores detallados si el servidor comienza a fallar.
*   **Download Data:** Permite descargar los resultados de la prueba en formato CSV para reportes de QA.
