#!/bin/bash

# Clone the repository
git clone https://github.com/masroor-ahmed/ipinfo-tool.git

# Change directory to the cloned repository
cd ipinfo-tool

# Install required Python packages
pip install -r requirements.txt

# Run the Python script
python ipinfo_tool.py

# Clean up - remove the cloned repository (optional)
cd ..
rm -rf ipinfo-tool
