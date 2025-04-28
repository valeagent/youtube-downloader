#!/bin/bash

echo "Setting up user agent..."
echo "Please visit https://whatmyuseragent.com/ to get your user agent string"
read -p "Enter your user agent string: " user_agent

# Create config.json with user agent
echo "{\"user_agent\": \"$user_agent\"}" > config.json

echo "User agent setup complete!" 