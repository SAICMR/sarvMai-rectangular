@echo off
REM Setup script for Tiling Calculator Project on Windows

echo.
echo ====================================
echo Tiling Calculator - Setup & Launch
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Python found. Setting up virtual environment...
cd backend

REM Create venv if it doesn't exist
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM Activate venv
call venv\Scripts\activate.bat

echo [2/4] Installing Python dependencies...
pip install -r requirements.txt

echo.
echo [3/4] Starting Backend API on http://localhost:5000...
echo.
start python app.py

timeout /t 3

echo.
echo [4/4] Opening Frontend UI in browser...
echo.
cd ..
start frontend\index.html

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo Backend API: http://localhost:5000
echo Frontend UI: Check your default browser
echo.
echo To stop the backend, close the API window.
echo.
pause
