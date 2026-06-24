# Informe de Pruebas de Carga con k6

Este informe documenta los resultados de las pruebas de carga ejecutadas contra el servidor Django local en http://127.0.0.1:8000/ping/.

## 📊 Tabla de Escalado Progresivo

| VUs | Duración | Peticiones Totales | Fallos (%) | p(95) Duración | ¿Aceptable? |
|-----|----------|-------------------|------------|----------------|-------------|
| 10 | 15s | 150 | 0.00% | 16.74ms | ✅ Sí |
| 30 | 15s | 450 | 4.88% | 13.26ms | ❌ No |
| 50 | 15s | 750 | 9.46% | 20.61ms | ❌ No |
| 80 | 15s | 1200 | 17.83% | 19.47ms | ❌ No |

## ⚙️ Pruebas Avanzadas y de Ramping

### 1. Prueba Avanzada (load_test_advanced.js)
- **Resultado**: ✅ Pasó (Thresholds superados)
- **Configuración**: 20 VUs, 30s. Thresholds: http_req_duration: p(95)<200ms, http_req_failed: rate<1%.

### 2. Prueba con Ramping (load_test_ramping.js)
- **Configuración**: Ramping progresivo hasta 90 VUs en 4 minutos.
- **Observaciones**: Registra el comportamiento del servidor de desarrollo de Django bajo carga incremental.

## 📝 Conclusiones
- El servidor de desarrollo de Django (unserver) es monohilo por defecto (a menos que se use multithread).
- Soporta adecuadamente cargas ligeras concurrentes (hasta ~30 VUs).
- Para concurrencias superiores a 50 VUs, comienza a aumentar el tiempo de respuesta y la tasa de fallos de conexión (timeout / connection refused).
- Se recomienda el despliegue con un servidor WSGI de producción (Gunicorn / Uvicorn + Nginx) para entornos productivos reales.
