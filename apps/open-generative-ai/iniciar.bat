@echo off
chcp 65001 >nul
title Open Generative AI - Estúdio Criativo Multimodal
echo.
echo ======================================================
echo    OPEN GENERATIVE AI - ESTÚDIO DE VÍDEO E VOZ
echo    Plataforma Aberta de Imagem, Áudio e Lip-Sync
echo ======================================================
echo.

cd /d "%~dp0"

where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [x] ERRO: Node.js nao encontrado no sistema!
    pause
    exit /b 1
)

set "TARGET_DIR=..\..\.agent\skills\open-generative-ai"
if not exist "%TARGET_DIR%\package.json" (
    echo [x] Codigo-fonte do Open Generative AI nao encontrado em: %TARGET_DIR%
    pause
    exit /b 1
)

cd /d "%TARGET_DIR%"

if not exist "node_modules" (
    echo [*] Instalando dependencias (npm install)...
    call npm install
)

echo.
echo [*] Iniciando servidor Next.js em http://localhost:3000...
echo.

start "" "http://localhost:3000"
npm run dev

pause
