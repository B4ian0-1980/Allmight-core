@echo off
chcp 65001 >nul
title Book-to-Skill - Conversor de Livros em Conhecimento de IA
echo.
echo ======================================================
echo    BOOK-TO-SKILL - FÁBRICA DE SKILLS DE IA
echo    Converte Manuais, Livros e PDFs em Skills Prontas
echo ======================================================
echo.

cd /d "%~dp0"

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [x] ERRO: Python nao encontrado no sistema!
    pause
    exit /b 1
)

set "TARGET_DIR=..\..\.agent\skills\book-to-skill"
if not exist "%TARGET_DIR%\pyproject.toml" (
    echo [x] Codigo-fonte do Book-to-Skill nao encontrado em: %TARGET_DIR%
    pause
    exit /b 1
)

cd /d "%TARGET_DIR%"

if not exist "venv\Scripts\python.exe" (
    echo [*] Criando ambiente virtual venv...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [*] Instalando dependencias de extracao (PDF/Epub/CLI)...
    pip install pypdf ebooklib markdown typer rich
)

echo.
echo [*] Ambiente pronto!
echo [*] Digite o caminho completo do arquivo PDF ou EPUB para converter:
set /p "BOOK_PATH=Caminho do arquivo: "

if "%BOOK_PATH%"=="" (
    echo [!] Nenhum arquivo informado. Encerrando.
    pause
    exit /b 0
)

echo.
echo [*] Processando arquivo: %BOOK_PATH%...
venv\Scripts\python.exe -m book_to_skill.cli "%BOOK_PATH%"

pause
