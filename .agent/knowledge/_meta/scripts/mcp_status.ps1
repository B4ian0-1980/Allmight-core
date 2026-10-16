# Script de Status dos Servidores MCP
# Data: 2026-02-15

Write-Host "[MCP Status] Verificando servicos..." -ForegroundColor Cyan
Write-Host "----------------------------------------" -ForegroundColor Gray

if (-Not (Test-Path ".mcp.pids.json")) {
    Write-Host "Arquivo .mcp.pids.json nao encontrado." -ForegroundColor Yellow
    Write-Host "Sugestao: Execute .\start_mcp_factory.ps1 primeiro." -ForegroundColor DarkGray
    exit
}

$pidsData = Get-Content ".mcp.pids.json" | ConvertFrom-Json
$statusList = @()

foreach ($key in $pidsData.PSObject.Properties.Name) {
    $pidNum = $pidsData.$key
    
    $isRunning = $false
    try {
        $proc = Get-Process -Id $pidNum -ErrorAction Stop
        $isRunning = $true
        $cpu = $proc.CPU
        $mem = [math]::Round($proc.WorkingSet / 1MB, 2)
    }
    catch {
        $isRunning = $false
    }
    
    $statusObj = [PSCustomObject]@{
        "Servidor"   = $key
        "PID"        = $pidNum
        "Status"     = if ($isRunning) { "RUNNING" } else { "STOPPED" }
        "Memory(MB)" = if ($isRunning) { $mem } else { "-" }
    }
    
    $statusList += $statusObj
}

# Exibir Tabela
$statusList | Format-Table -AutoSize

Write-Host "----------------------------------------" -ForegroundColor Gray
