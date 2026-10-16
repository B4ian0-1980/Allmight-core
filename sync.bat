@echo off
setlocal enabledelayedexpansion

echo ======================================================================
echo   ANTIGRAVITY KIT -- SINCRONIZACAO AUTOMATICA TOTAL DO SISTEMA
echo ======================================================================
echo.

:: 1. Garantir Junction .agents -> .agent (essencial para o Antigravity IDE)
if not exist "%~dp0.agents" (
    echo [*] Criando link de compatibilidade .agents para o Antigravity IDE...
    mklink /J "%~dp0.agents" "%~dp0.agent" >nul 2>&1
    if !errorlevel! equ 0 (
        echo [OK] Link .agents criado com sucesso.
    ) else (
        echo [-] Aviso: Nao foi possivel criar o link .agents automaticamente.
    )
)

:: 2. Garantir Diretrizes Globais em %USERPROFILE%\.gemini\GEMINI.md
if not exist "%USERPROFILE%\.gemini" mkdir "%USERPROFILE%\.gemini" >nul 2>&1
if not exist "%USERPROFILE%\.gemini\GEMINI.md" (
    if exist "%~dp0.agent\templates\GLOBAL_GEMINI.md" (
        echo [*] Restaurando diretrizes globais do agente em .gemini...
        copy /y "%~dp0.agent\templates\GLOBAL_GEMINI.md" "%USERPROFILE%\.gemini\GEMINI.md" >nul 2>&1
        echo [OK] Diretrizes globais restauradas com sucesso.
    )
)

:: 3. Detect valid working Python executable (prioritizes Python 3.13)
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    set "PY_CMD=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
) else if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PY_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
) else (
    where py >nul 2>&1
    if !errorlevel! equ 0 (
        set "PY_CMD=py -3.13"
    ) else (
        set "PY_CMD=python"
    )
)

echo Usando interpretador: !PY_CMD!
echo.

!PY_CMD! "%~dp0.agent\scripts\agent-cli.py" sync

echo.
echo ======================================================================
echo   Sincronizacao concluida com sucesso! Pressione qualquer tecla.
echo ======================================================================
pause
