# Script de Diagnostico e Limpeza Profunda (Doctor)
# Mata processos "fantasmas" do MCP para garantir um reinicio limpo.
# Autor: Antigravity Agent
# Data: 2026-02-16

$ErrorActionPreference = "SilentlyContinue"

Write-Host "========================================" -ForegroundColor Magenta
Write-Host "   MCP DOCTOR - DEEP CLEAN" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Magenta

# 1. Definir Assinaturas de Processos para Buscar
# Buscar por argumentos na linha de comando para não matar coisas erradas
$targets = @(
    @{ Name = "Django MCP"; Signature = "manage.py run_mcp" },
    @{ Name = "FastAPI MCP"; Signature = "server.py" },
    @{ Name = "Laravel MCP"; Signature = "mcp-server.php" },
    @{ Name = "Laravel Art"; Signature = "artisan mcp" },
    @{ Name = "Svelte MCP"; Signature = "@sveltejs/mcp" },
    @{ Name = "Angular MCP"; Signature = "@angular/cli mcp" },
    @{ Name = "Vite SSE"; Signature = "sse_bridge.py" },
    @{ Name = "Vite TSX"; Signature = "mcp-server.ts" },
    @{ Name = "Flask MCP"; Signature = "flask\server.py" }
)

# 2. Varredura WMI (Mais lento, mas vê linha de comando)
Write-Host "1. Escaneando processos ativos..." -ForegroundColor Cyan

$procs = Get-CimInstance Win32_Process | Select-Object ProcessId, Name, CommandLine

$killCount = 0

foreach ($p in $procs) {
    if (!$p.CommandLine) { continue }

    foreach ($t in $targets) {
        if ($p.CommandLine -like "*$($t.Signature)*") {
            Write-Host "   [MATCH] $($t.Name) encontrado (PID: $($p.ProcessId))" -ForegroundColor Yellow
            
            # Tenta Matar
            Stop-Process -Id $p.ProcessId -Force
            if ($?) {
                Write-Host "     -> ELIMINADO." -ForegroundColor Red
                $killCount++
            }
            else {
                Write-Host "     -> ERRO ao matar (Permissao?)" -ForegroundColor DarkRed
            }
        }
    }
}

# 3. Limpeza de Portas Famosas (Backup)
Write-Host "`n2. Verificando portas criticas..." -ForegroundColor Cyan
$ports = @(8000, 5173, 4200)

foreach ($port in $ports) {
    $conns = Get-NetTCPConnection -LocalPort $port 
    if ($conns) {
        foreach ($c in $conns) {
            $pidVal = $c.OwningProcess
            if ($pidVal -gt 0) {
                Write-Host "   [PORT $port] Ocupada por PID $pidVal. Tentando liberar..." -ForegroundColor Yellow
                Stop-Process -Id $pidVal -Force
                if ($?) { $killCount++ }
            }
        }
    }
}

# 4. Limpeza de Arquivo de PIDs Antigo
if (Test-Path ".mcp.pids.json") {
    Remove-Item ".mcp.pids.json"
    Write-Host "`n3. Arquivo .mcp.pids.json removido." -ForegroundColor Green
}

Write-Host "----------------------------------------" -ForegroundColor Gray
Write-Host "Limpeza Concluida. Processos mortos: $killCount" -ForegroundColor Green
Write-Host "Agora voce pode rodar: .\start_mcp_factory.ps1" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Magenta
