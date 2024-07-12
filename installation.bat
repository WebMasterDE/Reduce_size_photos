@echo off
SETLOCAL

echo Scaricando l'ultima versione di Python...

REM Definisci l'URL per scaricare l'ultima versione
SET "PYTHON_URL=https://www.python.org/ftp/python/"

REM Ottieni la pagina HTML per estrarre l'ultima versione
curl -s %PYTHON_URL% | findstr /R /C:"href=\"3.[0-9][0-9]*\""

REM Estrai l'ultima versione
FOR /F "tokens=2 delims=\" %%A IN ('curl -s %PYTHON_URL% ^| findstr /R /C:"href=\"3.[0-9][0-9]*\""') DO SET "LATEST_VERSION=%%A"

SET "PYTHON_INSTALLER=python-%LATEST_VERSION%-amd64.exe"

REM Scarica l'installer
curl -O %PYTHON_URL%%LATEST_VERSION%/%PYTHON_INSTALLER%

echo Installando Python...

REM Esegui l'installer in modalità silenziosa
start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Installazione completata.

REM Verifica se Python è installato
python --version
if ERRORLEVEL 1 (
    echo Python non è stato installato correttamente.
    exit /b 1
)

echo Installazione dei pacchetti richiesti...

REM Esegui pip install per installare i requisiti
pip install -r requirements.txt

echo Tutto completato.
ENDLOCAL
