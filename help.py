from consts import github_repo_link

def show_help():
    print(f"""NVM for Steam Deck help

Usage:

nvm list | -l               Lists all installed versions    
nvm install | -i <version>  Installs the specified version
nvm use | -u [version]      Uses the specified version (or .nvmrc if no version given)
nvm remove | -r <version>   Removes the specified version
nvm available | -a          Lists all available versions that can be downloaded from nodejs.org
nvm auto                    Auto-detect and switch to .nvmrc version (if present)
nvm help | -h               Shows help and usage of NVM for Steam Deck commands

.nvmrc support:
- Place a .nvmrc file in your project directory with the desired Node.js version
- Use 'nvm use' without arguments to automatically use the .nvmrc version
- Use 'nvm auto' to check and switch to .nvmrc version in current directory

For a more detailed documentation, visit NVM for Steam Deck repo: {github_repo_link}""")