$ErrorActionPreference = "Stop"

Set-Location -Path $PSScriptRoot

Write-Host "Checking Python..."
python --version | Out-Host

Write-Host "Installing server requirements..."
python -m pip install -r "..\server\requirements.txt"

Write-Host ""
Write-Host "Register local domain? (gncorpaice.local)"
$confirm = Read-Host "Type Y to add hosts entry"
if ($confirm -eq "Y" -or $confirm -eq "y") {
  $hostsPath = "$env:WINDIR\System32\drivers\etc\hosts"
  $entry = "127.0.0.1 gncorpaice.local"
  $content = Get-Content $hostsPath
  if ($content -notcontains $entry) {
    try {
      Add-Content -Path $hostsPath -Value $entry
      Write-Host "Added hosts entry: $entry"
    } catch {
      Write-Host "Failed to update hosts. Run this script as Administrator."
    }
  } else {
    Write-Host "Hosts entry already exists."
  }
}

Write-Host "Starting frontend server (http://localhost:8000)..."
Start-Process -NoNewWindow -WorkingDirectory ".." python -ArgumentList "-m http.server 8000"

Write-Host "Starting FastAPI server (http://localhost:8001)..."
python -m uvicorn server.app:app --host 0.0.0.0 --port 8001

Start-Process "http://localhost:8000/index.html"
