# AICE Associate - install Python if needed, then open official sample notebooks.
$ErrorActionPreference = "Continue"

function Refresh-Path {
  $machine = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
  $user = [System.Environment]::GetEnvironmentVariable("Path", "User")
  $env:Path = "$machine;$user"
}

function Test-PythonCmd {
  param($File, $PrefixArgs)
  try {
    $cmd = Get-Command $File -ErrorAction SilentlyContinue
    if (-not $cmd) { return $null }
    $allArgs = @()
    if ($PrefixArgs) { $allArgs += $PrefixArgs }
    $allArgs += "--version"
    $output = & $File @allArgs 2>&1 | Out-String
    if ($LASTEXITCODE -eq 0 -and $output -match "Python 3\.") {
      return @{ File = $File; PrefixArgs = @($PrefixArgs) }
    }
  } catch {
    return $null
  }
  return $null
}

function Find-Python {
  $candidates = @(
    @{ File = "py"; PrefixArgs = @("-3.12") },
    @{ File = "py"; PrefixArgs = @("-3.11") },
    @{ File = "py"; PrefixArgs = @("-3.10") },
    @{ File = "py"; PrefixArgs = @("-3") },
    @{ File = "python"; PrefixArgs = @() },
    @{ File = "python3"; PrefixArgs = @() }
  )
  foreach ($c in $candidates) {
    $hit = Test-PythonCmd -File $c.File -PrefixArgs $c.PrefixArgs
    if ($hit) { return $hit }
  }

  $paths = @(
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe",
    "$env:ProgramFiles\Python312\python.exe",
    "$env:ProgramFiles\Python311\python.exe"
  )
  foreach ($path in $paths) {
    if (Test-Path $path) {
      return @{ File = $path; PrefixArgs = @() }
    }
  }
  return $null
}

function Invoke-Python {
  param($Py, [string[]]$Args)
  $all = @()
  if ($Py.PrefixArgs) { $all += $Py.PrefixArgs }
  $all += $Args
  & $Py.File @all
  return $LASTEXITCODE
}

function Install-PythonRuntime {
  Write-Host "[1/3] Python not found. Installing Python 3.12 ..."
  Refresh-Path
  $winget = Get-Command winget -ErrorAction SilentlyContinue
  if ($winget) {
    Write-Host "Using winget..."
    winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
    Refresh-Path
    Start-Sleep -Seconds 2
    $found = Find-Python
    if ($found) { return $found }
  }

  Write-Host "Downloading official Python installer..."
  $installer = Join-Path $env:TEMP "python-3.12.10-amd64.exe"
  $url = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe"
  Invoke-WebRequest -Uri $url -OutFile $installer -UseBasicParsing
  Start-Process -FilePath $installer -ArgumentList @(
    "/quiet",
    "InstallAllUsers=0",
    "PrependPath=1",
    "Include_pip=1",
    "Include_launcher=1",
    "Include_test=0"
  ) -Wait
  Refresh-Path
  Start-Sleep -Seconds 2
  return (Find-Python)
}

$scriptRoot = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$root = (Resolve-Path (Join-Path $scriptRoot "..")).Path
Set-Location $root

if (-not (Test-Path (Join-Path $root "official_samples\regression\problem.ipynb"))) {
  Write-Host "official_samples not found. Run: git pull"
  exit 1
}

Write-Host "Project: $root"
Refresh-Path

$py = Find-Python
if (-not $py) {
  $py = Install-PythonRuntime
}
if (-not $py) {
  Write-Host "Python install failed. Install from https://www.python.org/downloads/ and check Add python.exe to PATH."
  exit 1
}

Write-Host ("Using: {0} {1}" -f $py.File, ($py.PrefixArgs -join " "))
Invoke-Python -Py $py -Args @("--version") | Out-Host

Write-Host "[2/3] Installing study libraries (first run can take several minutes)..."
$code = Invoke-Python -Py $py -Args @("-m", "pip", "install", "--upgrade", "pip")
$code = Invoke-Python -Py $py -Args @(
  "-m", "pip", "install",
  "numpy", "pandas", "matplotlib", "seaborn",
  "scikit-learn", "jupyter", "notebook", "ipykernel"
)
if ($code -ne 0) {
  Write-Host "Failed to install core libraries."
  exit 1
}

Write-Host "Installing TensorFlow (needed for Q13-Q14, optional if it fails)..."
Invoke-Python -Py $py -Args @("-m", "pip", "install", "tensorflow", "xgboost") | Out-Null

Invoke-Python -Py $py -Args @("-m", "ipykernel", "install", "--user", "--name", "aice", "--display-name", "Python (AICE)") | Out-Null

$nbDir = Join-Path $root "official_samples"
Write-Host "[3/3] Opening Jupyter at official_samples ..."
Write-Host "Open: regression/problem.ipynb  then  classification/problem.ipynb"
Write-Host "Stop Jupyter with Ctrl+C in this window."
Write-Host ""

$code = Invoke-Python -Py $py -Args @("-m", "notebook", "--notebook-dir=$nbDir")
exit $code
