# YouTube Downloader

### TLDR: Install ffmpeg -> double-click: setup_venv.bat -> double-click: start.bat

A user-friendly desktop application for downloading YouTube videos and audio using yt-dlp.

## Features

- Download YouTube videos in various qualities (mp4)
- Download audio-only (MP3)
- Support for age-restricted and private videos using cookies
- Simple and intuitive GUI interface
- Real-time download progress logging
- Dark theme with colored output
- Random geeky jokes to brighten your day!

## Prerequisites

- Python 3.11 or higher
- FFmpeg (required for audio extraction and format conversion)
- Get cookies using the [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/cclelndahbckbenkjhflpdbgdldlbecc?utm_source=item-share-cb) Chrome extension

## Installation

### Windows

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

2. Run the setup script (double-click the .bat File):
   ```bash
   setup_venv.bat
   ```

3. **User Agent Setup**:
   - During setup, you will be prompted to enter your browser's user agent.
   - Open your web browser (Chrome, Firefox, etc.) and visit [https://whatmyuseragent.com/](https://whatmyuseragent.com/).
   - Look for "User Agent" and copy the entire string.
   - Paste it into the terminal when prompted.

### Linux/Mac

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

2. Run the setup script:
   ```bash
   chmod +x setup_venv.sh
   ./setup_venv.sh
   ```

3. **User Agent Setup**:
   - During setup, you will be prompted to enter your browser's user agent.
   - Open your web browser (Chrome, Firefox, etc.) and visit [https://www.whatismybrowser.com/](https://www.whatismybrowser.com/).
   - Look for "User Agent" and copy the entire string.
   - Paste it into the terminal when prompted.

## FFmpeg Installation

### Windows
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract the files
3. Add the `bin` folder to your system PATH !

### Linux
```bash
sudo apt update
sudo apt install ffmpeg
```

### Mac
```bash
brew install ffmpeg
```

## Setup

1. Run `setup_venv.sh` (Linux/Mac) or `setup_venv.bat` (Windows)
2. Get your user agent from [whatmyuseragent.com](https://whatmyuseragent.com/)
3. Get cookies using the [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/cclelndahbckbenkjhflpdbgdldlbecc?utm_source=item-share-cb) Chrome extension
4. Start the application with `start.sh` (Linux/Mac) or `start.bat` (Windows)

## Usage

1. Start the application (double-click the .bat File):
   - Windows: Run `start.bat`
   - Linux/Mac: Run `./start.sh`

2. For age-restricted or private videos:
   - Install the "Get cookies.txt" Chrome extension
   - Log in to YouTube in Chrome
   - Click the extension icon and click "Copy" to copy all your cookies"
   - Paste the contents into the cookies text area in the application
   - Click "Save Cookies" !
   - (If dowload failed - delete the cookies in the text ares and paste new ones)

3. Enter the YouTube URL and select your desired format and media type
4. Click "Download"

## Common Issues and Solutions

### Download Failures

1. **Outdated yt-dlp**:
   - If you see errors about "This video is unavailable" or "Video unavailable", your yt-dlp version might be outdated
   - Solution: Run `pip install --upgrade yt-dlp` in your virtual environment

2. **Expired Cookies**:
   - YouTube cookies typically expire after 24 hours
   - If downloads start failing after working previously, try:
     1. Get fresh cookies using the "Get cookies.txt" extension
     2. Paste the new cookies into the application
     3. Click "Save Cookies"
     4. Try downloading again

3. **FFmpeg Issues**:
   - If you see errors about "ffmpeg not found", ensure FFmpeg is:
     1. Installed correctly
     2. Added to your system PATH
     3. Restart the application after installing FFmpeg
### Troubleshooting
- **Python not found**: Ensure Python 3.11+ is installed and in your system PATH
- **Cookies not working**: Get fresh cookies from the Chrome extension
- **User Agent Issues**: If downloads fail, try updating your user agent by running `setup_user_agent.bat` (Windows) or `./setup_user_agent.sh` (Linux/Mac) again

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 