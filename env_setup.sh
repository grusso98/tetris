#!/bin/bash

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found! Please make sure it's in the current directory."
    exit 1
fi

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Create a virtual environment in the directory 'venv'
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Install the requirements
echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt

# Confirm the setup
echo "Virtual environment setup complete and requirements installed."

# Note to the user on how to activate the virtual environment in future sessions
echo "To activate the virtual environment later, use: source venv/bin/activate"
