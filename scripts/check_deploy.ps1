# check_deploy.ps1 — Verificacion post-despliegue MIKITECH
$DOMAIN = "https://web-production-bfc004.up.railway.app"

$STATIC_FILES = @(
    "/static/css/main.css",
    "/static/css/admin_design_system.css",
    "/static/assets/index.js",
    "/static/assets/index.css",
    "/static/js/main.js",
    "/static/plantilla_carga_masiva_mikitech.xlsx"
)

$PAGES = @(
    "/",
    "/productos/",
    "/admin-panel/",
    "/cuenta/ingreso/"
)

Write-Host "`n====== VERIFICACION POST-DESPLIEGUE MIKITECH ======" -ForegroundColor Cyan
Write-Host "Dominio: $DOMAIN`n"

# Verificar archivos estaticos
Write-Host "--- ARCHIVOS ESTATICOS ---" -ForegroundColor Yellow
foreach ($file in $STATIC_FILES) {
    try {
        $response = Invoke-WebRequest -Uri "$DOMAIN$file" -Method Head -UseBasicParsing -TimeoutSec 10
        $status = $response.StatusCode
        if ($status -eq 200) {
            Write-Host "  OK  $file" -ForegroundColor Green
        } else {
            Write-Host "  WARN $file -> $status" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "  FAIL $file -> 404 o Error" -ForegroundColor Red
    }
}

# Verificar paginas principales
Write-Host "`n--- PAGINAS PRINCIPALES ---" -ForegroundColor Yellow
foreach ($page in $PAGES) {
    try {
        $response = Invoke-WebRequest -Uri "$DOMAIN$page" -Method Get -UseBasicParsing -TimeoutSec 15
        $status = $response.StatusCode
        if ($status -eq 200) {
            Write-Host "  OK  $page" -ForegroundColor Green
        } else {
            Write-Host "  WARN $page -> $status" -ForegroundColor Yellow
        }
    } catch {
        $code = $_.Exception.Response.StatusCode.value__
        if ($code -eq 302 -or $code -eq 301) {
            Write-Host "  OK  $page (redirect $code)" -ForegroundColor Green
        } else {
            Write-Host "  FAIL $page -> Error: $code" -ForegroundColor Red
        }
    }
}

Write-Host "`n====== VERIFICACION COMPLETA ======`n" -ForegroundColor Cyan
