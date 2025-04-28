@echo off
setlocal enabledelayedexpansion

echo YouTube Downloader Setup
echo ======================

:: Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not found in PATH. Please install Python 3.11+ and add it to PATH.
    pause
    exit /b 1
)

:: Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
for /f "tokens=1 delims=." %%i in ("%PYTHON_VERSION%") do set PYTHON_MAJOR=%%i
for /f "tokens=2 delims=." %%i in ("%PYTHON_VERSION%") do set PYTHON_MINOR=%%i

if %PYTHON_MAJOR% LSS 3 (
    echo Python 3.11+ is required. Found version %PYTHON_VERSION%
    pause
    exit /b 1
)

if %PYTHON_MINOR% LSS 11 (
    echo Python 3.11+ is required. Found version %PYTHON_VERSION%
    pause
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment
    pause
    exit /b 1
)

:: Activate virtual environment and install requirements
echo Installing requirements...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment
    pause
    exit /b 1
)

pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements
    pause
    exit /b 1
)

:: Check for ffmpeg
where ffmpeg >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo WARNING: FFmpeg is not found in PATH.
    echo Please install FFmpeg and add it to your system PATH.
    echo See README.md for installation instructions.
    echo.
)

:: Create downloads directory
if not exist downloads mkdir downloads

echo.
echo Setup completed successfully!
echo.
echo To start the application, run start.bat
echo.
pause 