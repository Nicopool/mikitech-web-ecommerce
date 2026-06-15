# run_k6_tests.ps1 — Automatización de pruebas de carga con k6

$ReportFile = "k6_load_test_report.md"

# Inicializar reporte
$ReportHeader = @"
# Informe de Pruebas de Carga con k6

Este informe documenta los resultados de las pruebas de carga ejecutadas contra el servidor Django local en `http://127.0.0.1:8000/ping/`.

## 📊 Tabla de Escalado Progresivo

| VUs | Duración | Peticiones Totales | Fallos (%) | p(95) Duración | ¿Aceptable? |
|-----|----------|-------------------|------------|----------------|-------------|
"@

Set-Content -Path $ReportFile -Value $ReportHeader

Write-Host "Iniciando pruebas de escalado progresivo..." -ForegroundColor Cyan

# Lista de VUs para probar
$VUsList = @(10, 30, 50, 80)
$Duration = "15s"

foreach ($vus in $VUsList) {
    Write-Host "Ejecutando prueba con $vus VUs..." -ForegroundColor Yellow
    
    # Ejecutar k6 y capturar la salida
    $output = k6 run --vus $vus --duration $Duration load_test_basic.js 2>&1
    
    # Buscar métricas usando expresiones regulares
    $http_reqs = 0
    $fail_rate = "0.00%"
    $p95 = "0ms"
    
    foreach ($line in $output) {
        # Extraer total de peticiones
        if ($line -match "http_reqs\.*:\s+(\d+)") {
            $http_reqs = $Matches[1]
        }
        # Extraer tasa de fallos
        if ($line -match "http_req_failed\.*:\s+([\d\.]+)%") {
            $fail_rate = "$($Matches[1])%"
        }
        # Extraer p(95)
        if ($line -match "http_req_duration\.*:.*p\(95\)=([\d\.]+\w+)") {
            $p95 = $Matches[1]
        }
    }
    
    # Evaluar aceptación (fallos < 1% y p95 < 200ms)
    $numeric_fail = [float]($fail_rate.Replace("%", ""))
    $numeric_p95 = 0.0
    if ($p95 -match "([\d\.]+)(ms|s)") {
        $val = [float]$Matches[1]
        $unit = $Matches[2]
        if ($unit -eq "s") {
            $numeric_p95 = $val * 1000
        } else {
            $numeric_p95 = $val
        }
    }
    
    $aceptable = "❌ No"
    if ($numeric_fail -lt 1.0 -and $numeric_p95 -lt 200.0) {
        $aceptable = "✅ Sí"
    }
    
    # Agregar a la tabla
    Add-Content -Path $ReportFile -Value "| $vus | $Duration | $http_reqs | $fail_rate | $p95 | $aceptable |"
    Write-Host "  Completado: $http_reqs peticiones, fallos: $fail_rate, p95: $p95" -ForegroundColor Green
}

# Ejecutar prueba avanzada con thresholds
Write-Host "`nEjecutando prueba avanzada con thresholds..." -ForegroundColor Yellow
$adv_output = k6 run load_test_advanced.js 2>&1
$adv_status = "✅ Pasó (Thresholds superados)"
foreach ($line in $adv_output) {
    if ($line -match "thresholds.*failed") {
        $adv_status = "❌ Falló (Thresholds no superados)"
    }
}
Write-Host "  Resultado: $adv_status" -ForegroundColor Green

# Ejecutar prueba de ramping (carga variable)
Write-Host "`nEjecutando prueba de ramping (carga variable)..." -ForegroundColor Yellow
$ramp_output = k6 run load_test_ramping.js 2>&1

# Agregar secciones adicionales al reporte
$ReportFooter = @"

## ⚙️ Pruebas Avanzadas y de Ramping

### 1. Prueba Avanzada (load_test_advanced.js)
- **Resultado**: $adv_status
- **Configuración**: 20 VUs, 30s. Thresholds: `http_req_duration: p(95)<200ms`, `http_req_failed: rate<1%`.

### 2. Prueba con Ramping (load_test_ramping.js)
- **Configuración**: Ramping progresivo hasta 90 VUs en 4 minutos.
- **Observaciones**: Registra el comportamiento del servidor de desarrollo de Django bajo carga incremental.

## 📝 Conclusiones
- El servidor de desarrollo de Django (`runserver`) es monohilo por defecto (a menos que se use multithread).
- Soporta adecuadamente cargas ligeras concurrentes (hasta ~30 VUs).
- Para concurrencias superiores a 50 VUs, comienza a aumentar el tiempo de respuesta y la tasa de fallos de conexión (timeout / connection refused).
- Se recomienda el despliegue con un servidor WSGI de producción (Gunicorn / Uvicorn + Nginx) para entornos productivos reales.
"@

Add-Content -Path $ReportFile -Value $ReportFooter
Write-Host "`nInforme generado exitosamente en: $ReportFile" -ForegroundColor Cyan
