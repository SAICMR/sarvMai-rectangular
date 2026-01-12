# PowerShell Setup Script for Tiling Calculator Project

Write-Host ""
Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Tiling Calculator - Setup & Launch" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[✓] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[✗] ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7+ from https://www.python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Navigate to backend
Push-Location backend

Write-Host "[1/4] Setting up virtual environment..." -ForegroundColor Yellow

# Create venv if it doesn't exist
if (-not (Test-Path "venv")) {
    Write-Host "Creating new virtual environment..." -ForegroundColor Gray
    python -m venv venv
    Write-Host "[✓] Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "[✓] Virtual environment already exists" -ForegroundColor Green
}

# Activate venv
& ".\venv\Scripts\Activate.ps1"

Write-Host "[2/4] Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "[3/4] Starting Backend API on http://localhost:5000..." -ForegroundColor Yellow
Write-Host ""

# Start Flask app in background job
$backendJob = Start-Job -ScriptBlock {
    python app.py
}

Start-Sleep -Seconds 3

Write-Host "[4/4] Opening Frontend UI in browser..." -ForegroundColor Yellow
Write-Host ""

# Open frontend in default browser
$frontendPath = (Get-Location).Path
$frontendPath = $frontendPath.Replace("\backend", "") + "\frontend\index.html"
Start-Process $frontendPath

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend API: http://localhost:5000" -ForegroundColor Cyan
Write-Host "Frontend UI: Check your default browser" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend is running in a background job." -ForegroundColor Yellow
Write-Host "To stop the backend, use: Stop-Job -Id $($backendJob.Id)" -ForegroundColor Gray
Write-Host ""

Pop-Location

Write-Host "Press Enter to exit..." -ForegroundColor Gray
Read-Host
