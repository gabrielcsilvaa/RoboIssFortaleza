@echo off
cd /d "%~dp0.."
set REQUIREMENTS_FILE=requirements.txt
python -m pip install -r %REQUIREMENTS_FILE%

IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao instalar os pacotes.
    exit /b %ERRORLEVEL%
) ELSE (
    echo Instalacao concluida com sucesso!
)
