#!/bin/bash

# NVM Removal Script
# This script runs the Python setup removal and reloads the shell environment

echo "🗑️  Starting NVM removal..."
echo

# Run the Python setup script with remove argument
python setup.py remove
setup_exit_code=$?

# Check if removal was successful
if [ $setup_exit_code -eq 0 ]; then
    echo
    echo "🎉 NVM has been removed from your system!"
    echo "💡 If you want to reinstall NVM later, just run: ./setup.sh"
    echo
    echo "🔄 Starting new shell session with updated environment..."
    
    # Replace current shell with new one that has the updated environment
    exec bash
else
    echo "❌ Removal failed. Please check the error messages above."
    exit 1
fi
