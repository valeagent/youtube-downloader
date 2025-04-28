@echo off
if not exist venv (
    echo Virtual environment not found. Running setup...
    setup_venv.bat
    if errorlevel 1 (
        pause
        exit /b 1
    )
)

:: Run the application without showing a terminal window
start /b pythonw main.py 