@echo off
chcp 65001 >nul
title LLaMA-Factory - Estúdio Visual de Treinamento de LLMs
echo.
echo ======================================================
echo    LLAMA-FACTORY - ESTÚDIO DE FINE-TUNING DE LLMS
echo    Treinamento Visual Sem Código de Modelos Abertos
echo ======================================================
echo.

cd /d "%~dp0"

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [x] ERRO: Python nao foi encontrado no sistema!
    pause
    exit /b 1
)

set "TARGET_DIR=..\..\.agent\skills\LlamaFactory"
if not exist "%TARGET_DIR%\pyproject.toml" (
    echo [x] Codigo-fonte do LLaMA-Factory nao encontrado em: %TARGET_DIR%
    pause
    exit /b 1
)

cd /d "%TARGET_DIR%"

if not exist "venv\Scripts\python.exe" (
    echo [*] Criando ambiente virtual venv...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [*] Instalando dependencias básicas do LLaMA-Factory...
    pip install -e .[metrics,bitsandbytes]
)

echo.
echo [*] Iniciando a WebUI do LLaMA-Factory em http://localhost:7860...
echo.

start "" "http://localhost:7860"
venv\Scripts\python.exe -m llamafactory.webui.interface

pause
