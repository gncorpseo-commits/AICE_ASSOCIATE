$ErrorActionPreference = "Stop"

$scriptRoot = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if (-not $scriptRoot) {
  $scriptRoot = (Get-Location).Path
}
$root = Resolve-Path (Join-Path $scriptRoot "..")
if (-not (Test-Path (Join-Path $root "server\requirements.txt"))) {
  Write-Host "Project files not found next to this script."
  Write-Host "Downloading latest project zip..."
  $tempRoot = if ($env:TEMP) { $env:TEMP } else { [IO.Path]::GetTempPath() }
  $zipPath = Join-Path $tempRoot "AICE_ASSOCIATE.zip"
  $extractRoot = Join-Path $tempRoot "AICE_ASSOCIATE"
  Invoke-WebRequest "https://github.com/gncorpseo-commits/AICE_ASSOCIATE/archive/refs/heads/main.zip" -OutFile $zipPath -UseBasicParsing
  if (Test-Path $extractRoot) {
    Remove-Item -Recurse -Force $extractRoot
  }
  Expand-Archive -Path $zipPath -DestinationPath $tempRoot -Force
  $expanded = Join-Path $tempRoot "AICE_ASSOCIATE-main"
  if (Test-Path $expanded) {
    Rename-Item $expanded "AICE_ASSOCIATE" -Force
  }
  $root = $extractRoot
}

Set-Location -Path $root

Write-Host "Checking Python..."
py -3.11 --version | Out-Host

Write-Host "Installing server requirements..."
py -3.11 -m pip install -r (Join-Path $root "server\requirements.txt")

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
Start-Process -NoNewWindow -WorkingDirectory $root py -ArgumentList "-3.11 -m http.server 8000"

Start-Process "http://localhost:8000/index.html"

Write-Host "Starting FastAPI server (http://localhost:8001)..."
py -3.11 -m uvicorn server.app:app --host 0.0.0.0 --port 8001
