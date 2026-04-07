@echo off
setlocal

cd /d "%~dp0"

echo Checking Python...
python --version
if errorlevel 1 (
  echo Python not found. Please install Python 3.11 and try again.
  pause
  exit /b 1
)

echo Installing server requirements...
python -m pip install -r "..\server\requirements.txt"
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
start "" cmd /c "cd /d .. && py -3.11 -m http.server 8000"

start http://localhost:8000/index.html
echo Keeping this window open for FastAPI...

echo Starting FastAPI server (http://localhost:8001)...
cd /d ..
py -3.11 -m uvicorn server.app:app --host 0.0.0.0 --port 8001

endlocal
