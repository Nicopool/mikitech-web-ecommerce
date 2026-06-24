# Guía de Pruebas de Carga con k6 para MIKITECH

Esta guía describe cómo instalar, configurar y ejecutar las pruebas de carga utilizando **k6** para evaluar el rendimiento del endpoint de la aplicación MIKITECH.

---

## 📋 1. ¿Qué es k6?
k6 es una herramienta de pruebas de carga de código abierto, desarrollada en Go, de alta eficiencia y orientada a desarrolladores. Te permite escribir scripts de prueba en JavaScript y ejecutarlos en consola de forma ultra-rápida, con un consumo mínimo de recursos (CPU y RAM).

---

## 🚀 2. Instalación de k6 en Windows

Tienes tres formas sencillas de instalar k6 en Windows:

### Opción A: A través de Winget (Recomendado)
Abre PowerShell o CMD y ejecuta:
```powershell
winget install g壓z.k6
```

### Opción B: A través de Chocolatey
Si utilizas el gestor de paquetes Chocolatey:
```powershell
choco install k6
```

### Opción C: Descarga Directa
1. Ve a la página de lanzamientos oficiales en GitHub: [k6 Releases](https://github.com/grafana/k6/releases).
2. Descarga el instalador `.msi` para Windows x64.
3. Ejecuta el instalador y sigue los pasos del asistente.

*Una vez instalado, abre una nueva terminal y verifica la instalación escribiendo:*
```bash
k6 version
```

---

## 🛠️ 3. Las Pruebas de Carga Disponibles (k6)

Hemos restaurado 4 scripts de prueba en JavaScript en la raíz del proyecto, los cuales apuntan al servidor local en `http://127.0.0.1:8000`:

### 1. Prueba Básica (`load_test_basic.js`)
Realiza una prueba simple de carga estática enviando peticiones al endpoint `/ping/`.
*   **Usuarios Virtuales (VUs):** `20`
*   **Duración:** `30 segundos`
*   **Ejecución:**
    ```bash
    k6 run load_test_basic.js
    ```

### 2. Prueba Avanzada con Thresholds (`load_test_advanced.js`)
Define umbrales (Thresholds) de aceptación de rendimiento. Si se superan los límites, el test fallará automáticamente en la consola.
*   **Usuarios Virtuales (VUs):** `20`
*   **Duración:** `30 segundos`
*   **Límites de aceptación (Thresholds):**
    - El 95% de las peticiones deben durar menos de 200 ms (`p(95)<200`).
    - La tasa de errores de conexión debe ser inferior al 1% (`rate<0.01`).
*   **Ejecución:**
    ```bash
    k6 run load_test_advanced.js
    ```

### 3. Prueba de Escalado Variable / Ramping (`load_test_ramping.js`)
Incrementa progresivamente el número de usuarios virtuales concurrentes para simular carga escalonada (útil para pruebas de estrés y resistencia).
*   **Fases (Stages):**
    - Sube de 0 a 10 VUs en 1 minuto.
    - Sube a 30 VUs en otro minuto.
    - Sube a 60 VUs en otro minuto.
    - Sube a 90 VUs en otro minuto.
    - Baja a 0 VUs en 30 segundos.
*   **Límites de aceptación (Thresholds):**
    - El 95% de las peticiones deben durar menos de 500 ms (`p(95)<500`).
    - La tasa de errores de conexión debe ser inferior al 2% (`rate<0.02`).
*   **Ejecución:**
    ```bash
    k6 run load_test_ramping.js
    ```

### 4. Prueba del Endpoint de Verificación (`load_test_verificar.js`)
Realiza peticiones POST simulando el envío de solicitudes de autenticación/verificación de códigos.
*   **Usuarios Virtuales (VUs):** `10`
*   **Duración:** `30 segundos`
*   **Ejecución:**
    ```bash
    k6 run load_test_verificar.js
    ```

---

## 📊 4. Automatización y Reporte (PowerShell)

Para hacer más fácil el proceso, tienes disponible el script de automatización [run_k6_tests.ps1](file:///c:/Users/turca/Desktop/MIKITECH-APP/run_k6_tests.ps1). Este script automatiza todo el proceso:

1. Ejecuta progresivamente las pruebas con **10, 30, 50 y 80 usuarios concurrentes** durante 15 segundos cada una.
2. Analiza los resultados de cada ejecución en tiempo real.
3. Determina si el rendimiento es aceptable (fallos < 1% y p95 < 200ms).
4. Ejecuta la prueba avanzada con umbrales y la prueba de ramping variable.
5. Genera un reporte resumido en formato Markdown llamado **`k6_load_test_report.md`** en la raíz del proyecto.

### ¿Cómo ejecutar el script automatizado?
1. Asegúrate de tener corriendo tu servidor local (Waitress en el puerto 8000).
2. Abre PowerShell en la raíz del proyecto y ejecuta:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\run_k6_tests.ps1
   ```
3. Al finalizar, abre el archivo autogenerado `k6_load_test_report.md` para ver la tabla comparativa del comportamiento del servidor.
