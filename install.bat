@echo off

REM Define o nome do arquivo de dependências
set REQUIREMENTS_FILE=requirements.txt

REM Instala os pacotes listados no requirements.txt
python -m pip install -r %REQUIREMENTS_FILE%

IF %ERRORLEVEL% NEQ 0 (
    echo Erro ao instalar os pacotes.
    exit /b %ERRORLEVEL%
) ELSE (
    echo Instalação concluída com sucesso!
)