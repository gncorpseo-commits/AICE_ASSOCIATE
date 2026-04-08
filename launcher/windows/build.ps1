$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$launcher = Join-Path $root "launcher\windows\launcher.py"
$distDir = Join-Path $root "launcher\windows\dist"

Write-Host "Building Windows launcher..."
py -3.11 -m pip install --upgrade pip pyinstaller

if (Test-Path $distDir) {
  Remove-Item -Recurse -Force $distDir
}

py -3.11 -m PyInstaller `
  --onefile `
  --name "AICE_Launcher" `
  --distpath $distDir `
  --noconsole `
  $launcher

Write-Host "Build complete."
Write-Host "Output:" (Join-Path $distDir "AICE_Launcher.exe")
