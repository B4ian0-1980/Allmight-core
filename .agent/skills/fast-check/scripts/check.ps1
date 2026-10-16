param (
    [string]$TargetDir = "."
)

$status = 0

function Run-Check {
    param (
        [string]$Label,
        [scriptblock]$Action
    )
    try {
        $output = & $Action 2>&1
        if ($LASTEXITCODE -eq 0 -or $? -eq $true) {
            Write-Host "OK    $Label" -ForegroundColor Green
        } else {
            Write-Host "FALHA $Label" -ForegroundColor Red
            $output | Select-Object -First 15 | ForEach-Object { Write-Host "  $_" -ForegroundColor Yellow }
            $script:status = 1
        }
    } catch {
        Write-Host "ERRO  ${Label}: $_" -ForegroundColor Red
        $script:status = 1
    }
}

# 1. PHP Syntax Check (if PHP exists)
if (Get-Command php -ErrorAction SilentlyContinue) {
    Run-Check "PHP Sintaxe" {
        $phpFiles = Get-ChildItem -Path $TargetDir -Filter "*.php" -Recurse -Depth 3 -ErrorAction SilentlyContinue | Select-Object -First 20
        foreach ($f in $phpFiles) {
            $res = php -l $f.FullName 2>&1
            if ($LASTEXITCODE -ne 0) { throw $res }
        }
    }
}

# 2. Python Syntax Check (if Python exists)
if (Get-Command python -ErrorAction SilentlyContinue) {
    Run-Check "Python Sintaxe" {
        python -m compileall -q -f $TargetDir 2>&1
    }
}

exit $status
