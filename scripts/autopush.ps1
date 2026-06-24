# ============================================================
# autopush.ps1 - Auto-commit y push a GitHub para MIKITECH
# Uso:
#   .\autopush.ps1                              -> push rapido
#   .\autopush.ps1 -Mensaje "mi mensaje"        -> commit personalizado
#   .\autopush.ps1 -Observar                    -> watcher cada 30s
# ============================================================
param(
    [string]$Mensaje = "",
    [switch]$Observar
)

$REPO = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$RAMA = "main"

function Push-Cambios {
    param([string]$msg)

    Set-Location $REPO

    $status = git status --porcelain
    if (-not $status) {
        Write-Host "[OK] Sin cambios nuevos. Nada que subir." -ForegroundColor Green
        return
    }

    if (-not $msg) {
        $fecha = Get-Date -Format "yyyy-MM-dd HH:mm"
        $msg = "chore: auto-save $fecha"
    }

    Write-Host "" 
    Write-Host "[CAMBIOS] Archivos modificados:" -ForegroundColor Cyan
    git status --short

    git add --all
    git commit -m $msg
    git push origin $RAMA

    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "[PUSH OK] Subido a GitHub (rama: $RAMA)" -ForegroundColor Green
        Write-Host "          Commit: $msg" -ForegroundColor DarkGray
    } else {
        Write-Host "[ERROR] Fallo al hacer push. Verifica tu conexion o credenciales." -ForegroundColor Red
    }
}

if ($Observar) {
    Write-Host "[WATCHER] Modo automatico activo - guarda cada 30 segundos." -ForegroundColor Yellow
    Write-Host "          Presiona Ctrl+C para detener." -ForegroundColor DarkGray
    Write-Host ""
    while ($true) {
        Push-Cambios -msg $Mensaje
        Start-Sleep -Seconds 30
    }
} else {
    Push-Cambios -msg $Mensaje
}
