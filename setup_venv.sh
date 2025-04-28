#!/bin/bash

echo "YouTube Downloader Setup"
echo "======================"

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not found. Please install Python 3.11+"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ]; then
    echo "Python 3.11+ is required. Found version $PYTHON_VERSION"
    exit 1
fi

if [ "$PYTHON_MINOR" -lt 11 ]; then
    echo "Python 3.11+ is required. Found version $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment and install requirements
echo "Installing requirements..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment"
    exit 1
fi

pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install requirements"
    exit 1
fi

# Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo
    echo "WARNING: FFmpeg is not found in PATH."
    echo "Please install FFmpeg and add it to your system PATH."
    echo "See README.md for installation instructions."
    echo
fi

# Create downloads directory
mkdir -p downloads

# Setup user agent
echo
echo "Setting up user agent..."
chmod +x setup_user_agent.sh
./setup_user_agent.sh
if [ $? -ne 0 ]; then
    echo "Failed to setup user agent"
    exit 1
fi

echo
echo "Setup completed successfully!"
echo
echo "To start the application, run ./start.sh"
echo 