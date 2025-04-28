#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run setup_venv.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "WARNING: FFmpeg is not found in PATH."
    echo "Some features may not work properly."
    echo "Please install FFmpeg and add it to your system PATH."
    echo "See README.md for installation instructions."
    echo
    read -p "Press Enter to continue anyway..."
fi

# Start the application
python main.py 