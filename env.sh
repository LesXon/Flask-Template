#!/bin/bash

# chmod +x load.sh
chmod +x 1.sh

# Virtual environment name (you can change it if needed)
ENV_NAME="venv"

echo "🔧 Creating Python virtual environment in ./$ENV_NAME ..."

# Create virtual environment
python3 -m venv $ENV_NAME

# Check if it was created successfully
if [ -d "$ENV_NAME" ]; then
    echo "✅ Virtual environment created successfully."

    # Activate the virtual environment
    source "$ENV_NAME/bin/activate"
    echo "✅ Virtual environment activated. (use 'deactivate' to exit)"

    # Install dependencies if requirements.txt exists
    if [ -f "requirements.txt" ]; then
        echo "📦 Installing dependencies from requirements.txt ..."
        pip install --upgrade pip
        pip install -r requirements.txt
    else
        echo "📄 requirements.txt not found. You can install packages manually."
    fi

else
    echo "❌ Failed to create the virtual environment."
fi

./1.sh