# NVM for Steam Deck

A Node.js version manager designed specifically for Steam Deck's read-only file system.

## Key Features

- **🚀 Auto-switching**: Automatically switches Node.js versions based on `.nvmrc` files when opening terminals or changing directories
- **📦 Auto-install**: Prompts to automatically install missing versions when you try to use them
- **🏷️ LTS identification**: Clearly marks LTS versions with their codenames (Iron, Hydrogen, Gallium, etc.)
- **🔧 Easy setup/removal**: One-command installation and removal with automatic environment reloading
- **💾 Steam Deck optimized**: Works perfectly with Steam Deck's read-only file system

## Why not use the original NVM?

The Steam Deck uses a read-only file system, which makes installing the original NVM complicated and potentially risky. This lightweight Python-based alternative provides the same essential functionality without needing to modify system files.

**Why Python?** Python comes pre-installed on Steam Deck and is accessible through Konsole, making this solution simple and safe to use.

## How it works

This tool works by adding a simple configuration to your `.bashrc` file:

```bash
if [ -f ~/node/current_used_version ]; then
    NODE_VERSION=$(<~/node/current_used_version)
    export PATH="$HOME/node/node-v${NODE_VERSION}-linux-x64/bin:$PATH"
fi

alias nvm="python {getcwd()}/nvm.py"

# Auto-switch Node.js version based on .nvmrc when changing directories
nvm_auto_use() {
    if [ -f .nvmrc ]; then
        python {getcwd()}/nvm.py auto
    fi
}

# Hook into cd command to auto-detect .nvmrc
cd() {
    builtin cd "$@"
    nvm_auto_use
}

# Auto-detect .nvmrc when terminal starts (only for interactive shells)
if [[ $- == *i* ]]; then
    nvm_auto_use
fi
```

Here's what happens:

1. **Version tracking**: Creates a file that stores your currently active Node.js version
2. **Automatic PATH setup**: When you open a terminal, it reads the current version and adds Node.js binaries to your PATH
3. **Convenient alias**: Adds an `nvm` command that you can use from anywhere

The configuration is wrapped in comments so it can be cleanly removed later if needed.

## Easy setup and removal

This NVM includes convenient scripts that handle everything automatically:

- **`setup.sh`** - Installs NVM and makes it immediately available in your current terminal
- **`remove.sh`** - Completely removes NVM from your system

Both scripts automatically reload your environment, so you never need to manually restart your terminal or run source commands.

## Installation

1. Download and extract this tool to any folder you like
2. Open Konsole and navigate to the folder
3. Run the setup script:

```bash
./setup.sh
```

That's it! The script will:

- Configure your `.bashrc` file automatically
- Start a fresh terminal session with NVM ready to use
- No manual steps required!

**Manual installation**: If you prefer, you can run `python setup.py` instead, but you'll need to restart your terminal or run `source ~/.bashrc` afterward.

## Usage

Once installed, you can use all the standard NVM commands to manage Node.js versions:

### View available versions

```bash
nvm -a
# or
nvm available
```

Shows all Node.js versions you can install. Features:

- **LTS versions** are clearly marked with their codename (e.g., "LTS: Iron", "LTS: Hydrogen")
- **Installed versions** are marked with a left arrow `← (installed)` if you have the latest version of that major series installed

### Install a Node.js version

```bash
nvm install 20.18.3    # Install a specific version
nvm install latest     # Install the latest version
nvm install lts        # Install the latest LTS version
```

Versions are downloaded to `~/node` directory.

### List installed versions

```bash
nvm -l
# or  
nvm list
```

Shows all Node.js versions currently installed on your system.

### Switch to a version

```bash
nvm use 20.18.3        # Switch to a specific version
nvm use latest         # Switch to latest installed version
nvm use lts            # Switch to latest LTS installed version
nvm use                # Auto-detect and use version from .nvmrc file
```

**Auto-install feature**: If you try to use a version that isn't installed, NVM will ask if you'd like to install it automatically:

```bash
nvm use 18.20.4
# Version 18.20.4 not found.
# Would you like to install Node.js 18.20.4? (y/N): y
# Installing Node.js 18.20.4...
# Now using version number 18.20.4
```

This works with both explicit versions and `.nvmrc` files, making it easy to get up and running in any project without manual installation steps.

**`.nvmrc` support**: Create a `.nvmrc` file in your project directory containing just the version number (like `20.18.3` or `v20.18.3`). When you run `nvm use` without arguments, it will automatically use the version specified in the `.nvmrc` file.

**Automatic version switching**: NVM automatically detects and switches Node.js versions in two scenarios:

- **On terminal startup**: When you open a new terminal, if there's a `.nvmrc` file in the current directory, NVM automatically switches to that version
- **When changing directories**: When you `cd` into a directory with a `.nvmrc` file, NVM automatically switches to that version

If the required version isn't installed, NVM will offer to install it automatically with your confirmation.

### Remove a version

```bash
nvm remove 20.18.3     # Remove a specific version
nvm remove latest      # Remove the latest version
nvm remove lts         # Remove the latest LTS version
```

**Note**: The `latest` and `lts` keywords always refer to the current latest/LTS versions from nodejs.org. If you installed a version when it was "latest" but it's no longer the latest, you may need to remove it by its specific version number.

### Get help

```bash
nvm -h
# or
nvm help
```

Shows help for all available commands.

### Auto-detect .nvmrc

```bash
nvm auto               # Manually check and switch to .nvmrc version
```

**Automatic detection**: NVM provides seamless automatic version switching:

- **Terminal startup**: When you open a new terminal, if there's a `.nvmrc` file in the current directory, NVM automatically switches to that version
- **Directory navigation**: When you `cd` into a directory with a `.nvmrc` file, NVM automatically switches to that version  
- **Auto-install**: If the required version isn't installed, NVM will offer to install it automatically with your confirmation

**Manual detection**: You can also manually trigger version detection:

```bash
nvm auto               # Manually check and switch to .nvmrc version
```

## .nvmrc File Format

Create a `.nvmrc` file in your project root with just the Node.js version:

```text
20.18.3
```

or with the 'v' prefix:

```text
v20.18.3
```

**Example workflow**:

1. Create `.nvmrc` in your project: `echo "20.18.3" > .nvmrc`
2. Navigate to your project directory - NVM automatically detects the version and offers to install it if needed
3. Accept installation when prompted, and you're ready to go!
4. Future visits to the directory will automatically switch to the correct version

**Seamless development**: Once set up, you never need to manually switch Node.js versions again. Just navigate to your projects and NVM handles everything automatically.

## Uninstalling

To completely remove NVM from your Steam Deck:

```bash
./remove.sh
```

This will:

- Remove all NVM configuration from your `.bashrc` file
- Start a fresh terminal session with NVM completely removed
- Clean removal with no manual steps required!

**Manual removal**: You can also run `python setup.py remove` if you prefer, but you'll need to restart your terminal or run `source ~/.bashrc` afterward.

**Note**: This only removes the NVM tool itself. If you want to delete your installed Node.js versions too, manually delete the `~/node` directory.

## Troubleshooting

If you encounter any problems:

1. **Make sure the scripts are executable**: Run `chmod +x setup.sh remove.sh`
2. **Check you're in the right directory**: The scripts need to be run from the folder where you extracted NVM
3. **Try manual installation**: If the scripts don't work, try `python setup.py` instead

For other issues, please create an issue on this project's GitHub repository.
