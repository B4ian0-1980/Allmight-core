@echo off
chcp 65001 >nul
title FreeLLMAPI - Gateway Gratuito de Modelos de IA
echo.
echo ======================================================
echo    FREELLMAPI - GATEWAY LOCAL DE MODELOS DE IA
echo    34 Provedores Gratuitos e 635 Modelos Unificados
echo ======================================================
echo.

cd /d "%~dp0"

:: 1. Verificar Node.js
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [x] ERRO: Node.js nao foi encontrado no sistema!
    echo     Instale o Node.js v20+ em: https://nodejs.org
    pause
    exit /b 1
)

:: 2. Localizar pasta do projeto
set "TARGET_DIR=..\..\.agent\skills\freellmapi"
if not exist "%TARGET_DIR%\package.json" (
    echo [x] Codigo-fonte do FreeLLMAPI nao encontrado em: %TARGET_DIR%
    pause
    exit /b 1
)

cd /d "%TARGET_DIR%"

:: 3. Verificar e instalar dependencias
if not exist "node_modules" (
    echo [*] Instalando dependencias do FreeLLMAPI (npm install)...
    call npm install
    if %errorlevel% neq 0 (
        echo [x] Falha ao instalar dependencias do Node.js.
        pause
        exit /b 1
    )
)

:: 4. Iniciar Servidor
echo.
echo [*] Iniciando o servidor FreeLLMAPI em http://localhost:3001...
echo [*] Endpoint compativel com OpenAI: http://localhost:3001/v1
echo.

start "" "http://localhost:3001"
npm run dev

pause
