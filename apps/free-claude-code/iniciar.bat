@echo off
chcp 65001 >nul
title Free Claude Code - Proxy de Modelos Abertos
echo.
echo ======================================================
echo    FREE CLAUDE CODE - PROXY DE MODELOS ABERTOS
echo    Roteador Local de LLMs Alternativos para Coding
echo ======================================================
echo.

cd /d "%~dp0"

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [x] ERRO: Python nao encontrado no sistema!
    pause
    exit /b 1
)

set "TARGET_DIR=..\..\.agent\skills\free-claude-code"
if not exist "%TARGET_DIR%\pyproject.toml" (
    echo [x] Codigo-fonte do Free Claude Code nao encontrado em: %TARGET_DIR%
    pause
    exit /b 1
)

cd /d "%TARGET_DIR%"

if not exist "venv\Scripts\python.exe" (
    echo [*] Criando ambiente virtual venv...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [*] Instalando dependencias do Proxy...
    pip install fastapi uvicorn httpx pydantic
)

echo.
echo [*] Iniciando Proxy do Free Claude Code na porta 8080...
echo [*] Configure o Claude Code / Aider para: http://localhost:8080/v1
echo.

venv\Scripts\python.exe -m uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload

pause
