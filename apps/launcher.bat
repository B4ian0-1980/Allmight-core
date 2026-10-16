@echo off
chcp 65001 >nul
title Central de Superferramentas - 0-Fonte

:MENU
cls
echo ======================================================================
echo          CENTRAL DE SUPERFERRAMENTAS EXECUTÁVEIS (0-FONTE)
echo ======================================================================
echo.
echo   [1] Git Web Hub         - Auditoria de Segredos e Publicador GitHub
echo   [2] FreeLLMAPI          - Gateway Gratuito de 635 Modelos de IA
echo   [3] MoneyPrinterTurbo   - Gerador de Vídeos Curtos (TikTok/Shorts)
echo   [4] LLaMA-Factory       - Estúdio Visual de Fine-Tuning de LLMs
echo   [5] Open Generative AI  - Estúdio Multimodal de Imagem, Vídeo e Voz
echo   [6] Free Claude Code    - Proxy Local para Claude Code com Modelos Abertos
echo   [7] Book-to-Skill       - Converter Livro/PDF em Conhecimento de IA
echo.
echo   [0] Sair
echo ======================================================================
echo.

set /p "OPCAO=Escolha uma opcao [0-7]: "

if "%OPCAO%"=="1" (
    echo [*] Iniciando Git Web Hub...
    start "" cmd /c "cd /d "%~dp0..\git-web-hub" & call iniciar.bat"
    goto MENU
)
if "%OPCAO%"=="2" (
    echo [*] Iniciando FreeLLMAPI...
    start "" cmd /c "cd /d "%~dp0freellmapi" & call iniciar.bat"
    goto MENU
)
if "%OPCAO%"=="3" (
    echo [*] Iniciando MoneyPrinterTurbo...
    start "" cmd /c "cd /d "%~dp0MoneyPrinterTurbo" & call iniciar.bat"
    goto MENU
)
if "%OPCAO%"=="4" (
    echo [*] Iniciando LLaMA-Factory...
    start "" cmd /c "cd /d "%~dp0LlamaFactory" & call iniciar.bat"
    goto MENU
)
if "%OPCAO%"=="5" (
    echo [*] Iniciando Open Generative AI...
    start "" cmd /c "cd /d "%~dp0open-generative-ai" & call iniciar.bat"
    goto MENU
)
if "%OPCAO%"=="6" (
    echo [*] Iniciando Free Claude Code...
    start "" cmd /c "cd /d "%~dp0free-claude-code" & call iniciar.bat"
    goto MENU
)
if "%OPCAO%"=="7" (
    echo [*] Iniciando Book-to-Skill...
    start "" cmd /c "cd /d "%~dp0book-to-skill" & call iniciar.bat"
    goto MENU
)
if "%OPCAO%"=="0" (
    exit /b 0
)

echo [!] Opcao invalida. Pressione qualquer tecla para tentar novamente.
pause >nul
goto MENU
