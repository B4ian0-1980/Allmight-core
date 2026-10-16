# Script para Gerenciamento da Fabrica de Servidores MCP
# Permite iniciar/reiniciar serviços individualmente ou em grupo.
# Autor: Antigravity Agent & User
# Data: 2026-02-16

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$pidsFile = ".mcp.pids.json"
$baseMcpPath = "servers\MCP-Server"
$root = Get-Location
$venvPython = "$root\servers\MCP-Server\.venv\Scripts\python.exe"

# --- Configuração dos Serviços ---
$services = @{
    "1" = @{ Name = "Django"; Path = "$baseMcpPath\django"; Cmd = "& '$venvPython' manage.py run_mcp" }
    "2" = @{ Name = "FastAPI"; Path = "$baseMcpPath\fastapi"; Cmd = "& '$venvPython' server.py" }
    "3" = @{ Name = "Laravel"; Path = "$baseMcpPath\laravel"; Cmd = "php mcp-server.php" }
    "4" = @{ Name = "Svelte"; Path = "$baseMcpPath\svelte"; Cmd = "cmd /c 'npm install && npx -y @sveltejs/mcp'" }
    "5" = @{ Name = "Angular"; Path = "$baseMcpPath\angular"; Cmd = "cmd /c 'npx -y @angular/cli mcp'" }
    "6" = @{ Name = "VueHub"; Path = "$baseMcpPath\vite"; Cmd = "cmd /c 'npm run dev'" }
    "7" = @{ Name = "Flask"; Path = "$baseMcpPath\flask"; Cmd = "& '$venvPython' server.py" }
}

# --- Funções Auxiliares ---

function Load-Pids {
    if (Test-Path $pidsFile) {
        $json = Get-Content $pidsFile | ConvertFrom-Json
        $hash = @{}
        if ($json) {
            foreach ($prop in $json.PSObject.Properties) {
                $hash[$prop.Name] = $prop.Value
            }
        }
        return $hash
    }
    return @{}
}

function Save-Pids ($data) {
    $data | ConvertTo-Json | Set-Content $pidsFile
}

function Stop-Server ($name, $currentPid) {
    if ($currentPid -and (Get-Process -Id $currentPid -ErrorAction SilentlyContinue)) {
        Write-Host "   [STOP] Parando $name (PID: $currentPid)..." -ForegroundColor DarkGray
        Stop-Process -Id $currentPid -Force -ErrorAction SilentlyContinue
    }
}

function Start-Server ($key) {
    $svc = $services[$key]
    $pidsData = Load-Pids

    # Para instância anterior se existir
    Stop-Server $svc.Name $pidsData[$svc.Name]

    Write-Host "   [START] Iniciando $($svc.Name)..." -ForegroundColor Cyan
    $fullPath = Join-Path $root $svc.Path
    
    # Lança o processo
    # Nota: Usamos powershell interno para invocar o comando e manter a janela oculta
    $p = Start-Process powershell -ArgumentList "-Command", "& {
        cd '$fullPath'
        $($svc.Cmd)
    }" -WindowStyle Hidden -PassThru

    if ($p) {
        Write-Host "     -> PID: $($p.Id)" -ForegroundColor Green
        $pidsData[$svc.Name] = $p.Id
        Save-Pids $pidsData
    }
    else {
        Write-Host "     -> ERRO ao iniciar $($svc.Name)" -ForegroundColor Red
    }
}

function Show-Menu {
    Clear-Host
    Write-Host "========================================" -ForegroundColor Magenta
    Write-Host "   ANTIGRAVITY MCP FACTORY CONTROL" -ForegroundColor White
    Write-Host "========================================" -ForegroundColor Magenta
    
    $pidsData = Load-Pids

    # Exibe Status Atual
    foreach ($key in 1..7) {
        $svc = $services["$key"]
        $pidVal = $pidsData[$svc.Name]
        $status = "OFF"
        $color = "Gray"
        
        if ($pidVal -and (Get-Process -Id $pidVal -ErrorAction SilentlyContinue)) {
            $status = "RUNNING ($pidVal)"
            $color = "Green"
        }

        Write-Host "  [$key] $($svc.Name)" -NoNewline
        Write-Host " - " -NoNewline
        Write-Host $status -ForegroundColor $color
    }
    
    Write-Host "----------------------------------------" -ForegroundColor Gray
    Write-Host "  [A] Iniciar/Reiniciar TODOS" -ForegroundColor Yellow
    Write-Host "  [K] Matar TODOS (Stop All)" -ForegroundColor Red
    Write-Host "  [Q] Sair" -ForegroundColor White
    Write-Host "========================================" -ForegroundColor Magenta
}

# --- Loop Principal ---

# Se passar argumentos, tenta executar direto (ex: .\script.ps1 -Target All)
param([string]$Target = "")

if ($Target -eq "All") {
    1..7 | ForEach-Object { Start-Server "$_" }
    exit
}

do {
    Show-Menu
    $selection = Read-Host "Escolha uma opcao"

    switch ($selection) {
        { $_ -in "1", "2", "3", "4", "5", "6", "7" } { 
            Start-Server $selection 
            Start-Sleep -Seconds 1
        }
        "A" { 
            Write-Host "Reiniciando TODOS..." -ForegroundColor Yellow
            1..7 | ForEach-Object { Start-Server "$_" }
            Start-Sleep -Seconds 2
        }
        "K" {
            Write-Host "Parando TODOS..." -ForegroundColor Red
            $pidsData = Load-Pids
            foreach ($key in $pidsData.Keys) {
                Stop-Server $key $pidsData[$key]
            }
            Remove-Item $pidsFile -ErrorAction SilentlyContinue
            Start-Sleep -Seconds 2
        }
        "Q" { 
            Write-Host "Saindo..."
            return
        }
    }
} while ($true)
