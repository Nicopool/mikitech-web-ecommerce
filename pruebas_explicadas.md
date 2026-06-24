# 🚀 Plan de Pruebas de Carga y Rendimiento con k6

Este documento detalla la suite completa de pruebas de carga implementada en **MIKITECH-APP** para evaluar y garantizar el rendimiento, la escalabilidad y la fiabilidad de la plataforma de comercio electrónico.

---

## 📊 1. Resumen de Pruebas Disponibles

La siguiente tabla resume los diferentes escenarios de prueba diseñados para la plataforma:

| Script de Prueba | Archivo | Endpoint Objetivo | Tipo de Carga | VUs Máx. | Duración | Propósito Principal |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **Básica Progresiva** | `load_test_basic.js` | `/ping/` | Concurrencia Fija | 10 a 80 | 15s/etapa | Determinar la capacidad máxima del servidor local. |
| **Avanzada con SLOs** | `load_test_advanced.js` | `/ping/` | Carga Estable | 20 | 30s | Evaluar tiempos bajo Acuerdos de Nivel de Servicio (SLOs). |
| **Escalado (Ramping)** | `load_test_ramping.js` | `/ping/` | Carga Variable | 90 | 4m 30s | Evaluar la respuesta del servidor en picos y descensos. |
| **Verificación OTP** | `load_test_verificar.js` | `/verificar/` | Carga Transaccional (POST) | 10 | 30s | Probar peticiones con envío de cuerpo de datos JSON. |
| **Ingreso (Login)** | `tests/k6/k6_login.js` | `/cuenta/ingreso/` | Autenticación Completa | 5 | 20s | Evaluar seguridad y manejo de tokens CSRF en concurrencia. |
| **Navegación Usuario**| `tests/k6/k6_load.js` | `/` y `/productos/` | Flujo de Cliente | 20 | 30s | Simular el comportamiento típico de exploración en tienda. |

---

## 🔍 2. Detalle de Cada Escenario de Prueba

### 📋 A. Prueba de Carga Básica (`load_test_basic.js`)
* **Propósito**: Mide la capacidad bruta de atención de peticiones concurrentes en un endpoint de respuesta ultra-rápida (`/ping/`).
* **Configuración**: Se ejecuta con incrementos controlados de usuarios virtuales (10, 30, 50, 80 VUs).
* **Parámetros**:
  - GET `http://127.0.0.1:8000/ping/`
  - Sleep de 1 segundo por ciclo.

### 📋 B. Prueba Avanzada con SLOs (`load_test_advanced.js`)
* **Propósito**: Comprobar si el backend cumple con umbrales rígidos de rendimiento aceptable (SLO).
* **Configuración**: 20 VUs constantes durante 30 segundos.
* **Umbrales Críticos**:
  - **Tasa de fallos (`http_req_failed`)**: `< 1%`
  - **Tiempo de respuesta p95 (`http_req_duration`)**: `< 200ms` (El 95% de las peticiones debe resolverse en menos de 200ms).

### 📋 C. Prueba con Ramping Variable (`load_test_ramping.js`)
* **Propósito**: Simula un comportamiento del mundo real donde el tráfico sube progresivamente en horas pico y desciende al terminar el evento.
* **Fases de Escalado**:
  1. **Subida Inicial**: De 0 a 10 VUs en 1 minuto.
  2. **Escalado Medio**: De 10 a 30 VUs en 1 minuto.
  3. **Pico de Carga**: De 30 a 60 VUs en 1 minuto.
  4. **Estrés Máximo**: De 60 a 90 VUs en 1 minuto.
  5. **Enfriamiento**: Reducción a 0 VUs en 30 segundos.
* **Umbrales**:
  - p(95) < 500ms
  - Fallos < 2%

### 📋 D. Prueba de Verificación OTP (`load_test_verificar.js`)
* **Propósito**: Evaluar la API de verificación enviando peticiones `POST` que simulan el ingreso de códigos OTP.
* **Configuración**: 10 VUs durante 30 segundos.
* **Flujo**:
  - Genera dinámicamente un correo electrónico según el ID del Usuario Virtual (`test${__VU}@test.com`).
  - Envía la estructura JSON correcta en el cuerpo de la petición.
  - Verifica que el código de respuesta sea 200 (éxito) o 400 (solicitud incorrecta o código inválido), pero no 500 (error del servidor).

### 📋 E. Prueba de Login / Autenticación (`tests/k6/k6_login.js`)
* **Propósito**: Simular el proceso de inicio de sesión de los clientes de MIKITECH, que es una operación costosa en términos de CPU (debido al hasheo de contraseñas y base de datos).
* **Flujo de Ejecución**:
  1. **Fase 1: Extracción del Token CSRF**: Realiza un `GET` a la vista de ingreso y extrae el token del input oculto `csrfmiddlewaretoken` usando expresiones regulares.
  2. **Fase 2: POST de Credenciales**: Envía las credenciales junto con el token y cabeceras adecuadas.
  3. **Comprobación**: Valida que retorne código 200 o redirección 302 (éxito de autenticación).

### 📋 F. Prueba de Navegación de Usuario (`tests/k6/k6_load.js`)
* **Propósito**: Modelar un recorrido de compra tradicional.
* **Flujo**:
  1. Accede a la página de Inicio (`/`).
  2. Hace una pausa de 1 segundo.
  3. Navega al catálogo general de productos (`/productos/`).
  4. Hace una pausa de 1 segundo.
* **Umbrales**:
  - p(95) de la duración del request < 300ms.
  - Tasa de errores < 1%.

---

## ⚡ 3. Resultados de la Última Ejecución Consolidados

Basado en la ejecución de control realizada en el servidor de desarrollo local:

### 📈 Tabla de Desempeño por Concurrencia
| VUs Concurrentes | Tasa de Peticiones | Peticiones Totales | Tasa de Fallos (%) | p(95) Duración (ms) | Diagnóstico |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **10 VUs** | 10 req/s | 150 | 0.00% | 16.74 ms | **Óptimo** (Excelente respuesta) |
| **30 VUs** | 30 req/s | 450 | 4.88% | 13.26 ms | **Saturación Leve** (Empiezan a perderse sockets) |
| **50 VUs** | 50 req/s | 750 | 9.46% | 20.61 ms | **Congestión** (Errores de conexión en aumento) |
| **80 VUs** | 80 req/s | 1200 | 17.83% | 19.47 ms | **Sobrecarga** (Múltiples timeouts locales) |

---

## 📝 4. Conclusiones y Diagnóstico Técnico

1. **Limitación de Desarrollo**: El servidor integrado de Django (`manage.py runserver`) está diseñado exclusivamente para propósitos de prueba locales. Al ser monohilo y no tener buffering de peticiones robusto, sufre desconexiones físicas (sockets rechazados) cuando la concurrencia supera los **30 VUs**.
2. **Excelente Latencia Interna**: Cuando el servidor logra procesar el paquete, el tiempo de respuesta es sumamente rápido (<20 ms). Esto comprueba que la lógica en Python y las respuestas JSON son muy eficientes.
3. **Recomendación para Producción**: Para soportar cargas reales superiores a 100 concurrentes sin fallos, es imprescindible:
   * Reemplazar `runserver` por un servidor WSGI/ASGI de grado de producción como **Waitress** o **Gunicorn**.
   * Habilitar un servidor proxy inverso como **Nginx** al frente para gestionar las colas de peticiones y balancear la carga.
