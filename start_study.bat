@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo === AICE Associate 학습 시작 ===
echo 첫 설치는 5~15분 걸릴 수 있습니다. 창을 닫지 마세요.
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup\start_study.ps1"
if errorlevel 1 (
  echo.
  echo 실패했습니다. 이 창을 닫지 말고 에러 문구를 남겨 주세요.
  pause
  exit /b 1
)
echo.
echo Jupyter를 종료하려면 이 창에서 Ctrl+C 를 누르세요.
pause
