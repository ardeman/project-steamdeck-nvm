#!/bin/bash

# NVM Setup Script
# This script runs the Python setup and then reloads the shell environment

echo "🚀 Starting NVM setup..."
echo

# Run the Python setup script
python setup.py "$@"
setup_exit_code=$?

# Check if setup was successful
if [ $setup_exit_code -eq 0 ]; then
    echo
    echo "🔄 Reloading shell environment..."
    
    echo "✅ Setup completed successfully!"
    echo
    echo "🎯 NVM is now ready to use! Try these commands:"
    echo "  nvm -a          # List available Node.js versions"
    echo "  nvm -i 20.18.3  # Install Node.js version 20.18.3"
    echo "  nvm -u 20.18.3  # Switch to Node.js version 20.18.3"
    echo "  nvm -l          # List installed versions"
    echo "  nvm -h          # Show help"
    echo
    echo "🔄 Starting new shell session with NVM loaded..."
    
    # Replace current shell with new one that has the updated environment
    exec bash
else
    echo "❌ Setup failed. Please check the error messages above."
    exit 1
fi
