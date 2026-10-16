@echo off
setlocal enabledelayedexpansion

:: Detect valid working Python executable (prioritizes Python 3.13)
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

!PY_CMD! "%~dp0.agent\scripts\agent-cli.py" %*
