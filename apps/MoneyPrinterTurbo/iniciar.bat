@echo off
chcp 65001 >nul
title MoneyPrinterTurbo - Gerador Automático de Vídeos Curtos
echo.
echo ======================================================
echo    MONEYPRINTERTURBO - GERADOR DE VÍDEOS CURTOS
echo    Vídeos com Roteiro, Áudio e Legendas para TikTok/Shorts
echo ======================================================
echo.

cd /d "%~dp0"

:: 1. Verificar Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [x] ERRO: Python nao foi encontrado no sistema!
    echo     Instale o Python 3.10+ adicionando-o ao PATH.
    pause
    exit /b 1
)

set "TARGET_DIR=..\..\.agent\skills\MoneyPrinterTurbo"
if not exist "%TARGET_DIR%\main.py" (
    echo [x] Codigo-fonte do MoneyPrinterTurbo nao encontrado em: %TARGET_DIR%
    pause
    exit /b 1
)

cd /d "%TARGET_DIR%"

:: 2. Verificar/Criar Ambiente Virtual
if not exist "venv\Scripts\python.exe" (
    echo [*] Criando ambiente virtual Python isolado em venv...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [*] Instalando dependencias (pip install)...
    pip install -r requirements.txt
)

:: 3. Iniciar WebUI
echo.
echo [*] Iniciando a interface visual do MoneyPrinterTurbo em http://localhost:8501...
echo.

start "" "http://localhost:8501"
if exist "webui.bat" (
    call webui.bat
) else (
    venv\Scripts\python.exe -m streamlit run webui/Main.py
)

pause
