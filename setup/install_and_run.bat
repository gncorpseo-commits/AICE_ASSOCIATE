@echo off
setlocal

set SCRIPT_DIR=%~dp0
set ROOT=%SCRIPT_DIR%..

if not exist "%ROOT%\server\requirements.txt" (
  echo Project files not found next to this script.
  echo Downloading latest project zip...
  set ZIP_PATH=%TEMP%\AICE_ASSOCIATE.zip
  set EXTRACT_ROOT=%TEMP%\AICE_ASSOCIATE
  powershell -NoProfile -Command "Invoke-WebRequest https://github.com/gncorpseo-commits/AICE_ASSOCIATE/archive/refs/heads/main.zip -OutFile '%ZIP_PATH%'; if (Test-Path '%EXTRACT_ROOT%') { Remove-Item -Recurse -Force '%EXTRACT_ROOT%' }; Expand-Archive -Path '%ZIP_PATH%' -DestinationPath '%TEMP%'; if (Test-Path '%TEMP%\\AICE_ASSOCIATE-main') { Rename-Item '%TEMP%\\AICE_ASSOCIATE-main' 'AICE_ASSOCIATE' }"
  set ROOT=%EXTRACT_ROOT%
)

echo Checking Python...
py -3.11 --version
if errorlevel 1 (
  echo Python not found. Please install Python 3.11 and try again.
  pause
  exit /b 1
)

echo Installing server requirements...
py -3.11 -m pip install -r "%ROOT%\server\requirements.txt"
if errorlevel 1 (
  echo Failed to install requirements.
  pause
  exit /b 1
)

echo.
set /p ADDHOST=Add local domain (gncorpaice.local)? [Y/N]:
if /I "%ADDHOST%"=="Y" (
  set HOSTS_FILE=%WINDIR%\System32\drivers\etc\hosts
  findstr /C:"127.0.0.1 gncorpaice.local" "%HOSTS_FILE%" >nul
  if errorlevel 1 (
    echo 127.0.0.1 gncorpaice.local>>"%HOSTS_FILE%"
    if errorlevel 1 (
      echo Failed to update hosts. Run this script as Administrator.
    ) else (
      echo Hosts entry added.
    )
  ) else (
    echo Hosts entry already exists.
  )
)

echo Starting frontend server (http://localhost:8000)...
start "" cmd /c "cd /d %ROOT% && py -3.11 -m http.server 8000"

start http://localhost:8000/index.html
echo Keeping this window open for FastAPI...

echo Starting FastAPI server (http://localhost:8001)...
cd /d %ROOT%
py -3.11 -m uvicorn server.app:app --host 0.0.0.0 --port 8001

endlocal
