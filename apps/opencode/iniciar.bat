@echo off
setlocal
chcp 65001 >nul

echo ===================================================
echo     🚀 OpenCode v2 - Assistente de Codigo IA
echo ===================================================
echo.

:: 1. Verificar se Node.js esta instalado
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Node.js nao foi encontrado no sistema!
    echo Instale o Node.js v18+ em: https://nodejs.org/
    pause
    exit /b 1
)

:: 2. Verificar se opencode ja esta disponivel
where opencode >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] OpenCode CLI encontrado globalmente.
    echo Iniciando OpenCode v2...
    echo.
    opencode %*
    goto :end
)

:: 3. Executar via npx direto sem necessidade de instalacao global
echo [INFO] Executando OpenCode v2 via npx...
echo.
call npx --yes opencode-ai@latest %*

:end
if %errorlevel% neq 0 (
    echo.
    echo Se desejar instalar globalmente, execute:
    echo   npm install -g opencode-ai
)
endlocal
