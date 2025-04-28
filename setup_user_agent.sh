#!/bin/bash

echo "YouTube Downloader - User Agent Setup"
echo "===================================="

echo
echo "To download videos, we need your browser's user agent."
echo "Please follow these steps:"
echo
echo "1. Open your web browser (Chrome, Firefox, etc.)"
echo "2. Visit https://www.whatismybrowser.com/"
echo "3. Look for 'User Agent' and copy the entire string"
echo "4. Paste it below when prompted"
echo

read -p "Enter your user agent: " user_agent

if [ -z "$user_agent" ]; then
    echo "No user agent provided. Using default."
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
fi

echo
echo "Saving user agent to config.json..."
echo

echo "{ \"user_agent\": \"$user_agent\" }" > config.json

echo "User agent setup completed!"
echo 