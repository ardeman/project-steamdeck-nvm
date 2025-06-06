from os import path, system, getcwd
from sys import argv
from list import get_node_versions

def read_nvmrc(directory=None):
    """Read .nvmrc file from the given directory or current directory"""
    if directory is None:
        directory = getcwd()
    
    nvmrc_path = path.join(directory, '.nvmrc')
    if path.exists(nvmrc_path):
        try:
            with open(nvmrc_path, 'r') as f:
                version = f.read().strip()
                # Remove 'v' prefix if present (e.g., v20.18.3 -> 20.18.3)
                if version.startswith('v'):
                    version = version[1:]
                return version
        except Exception as e:
            print(f"Error reading .nvmrc: {e}")
            return None
    return None

def use_node_version():
    # If no version argument provided, try to read from .nvmrc
    if len(argv) <= 2:
        version_from_nvmrc = read_nvmrc()
        if version_from_nvmrc:
            version_number = version_from_nvmrc
            print(f"Found .nvmrc with version {version_number}")
        else:
            print("Version argument is needed, or create a .nvmrc file with the desired version.")
            exit()
    else:
        version_number = argv[2]
    
    if (get_node_versions().count(version_number) != 0):
        f = open(path.expanduser("~/node/current_used_version"), "w")
        f.write(version_number)
        print(f"Now using version number {version_number}")
        print("Make sure to source/reload your terminal with 'source ~/.bashrc'")
    else:
        print(f"Version {version_number} not found.")
        
        # Ask user if they want to install the missing version
        try:
            response = input(f"Would you like to install Node.js {version_number}? (y/N): ").strip().lower()
            if response in ['y', 'yes']:
                print(f"Installing Node.js {version_number}...")
                # Import install function and call it
                from install import install_node_version
                # Temporarily modify argv to simulate 'nvm install <version>'
                original_argv = argv.copy()
                argv.clear()
                argv.extend(['nvm.py', 'install', version_number])
                try:
                    install_node_version()
                    # After successful installation, use the version
                    f = open(path.expanduser("~/node/current_used_version"), "w")
                    f.write(version_number)
                    print(f"Now using version number {version_number}")
                    print("Make sure to source/reload your terminal with 'source ~/.bashrc'")
                except SystemExit:
                    # install_node_version() calls exit(), so we catch it and continue
                    # Check if installation was successful
                    if get_node_versions().count(version_number) != 0:
                        f = open(path.expanduser("~/node/current_used_version"), "w")
                        f.write(version_number)
                        print(f"Now using version number {version_number}")
                        print("Make sure to source/reload your terminal with 'source ~/.bashrc'")
                    else:
                        print("Installation failed.")
                        exit()
                finally:
                    # Restore original argv
                    argv.clear()
                    argv.extend(original_argv)
            else:
                print("Installation cancelled.")
                if len(argv) <= 2:  # Was read from .nvmrc
                    print(f"You can install it later with: nvm install {version_number}")
                exit()
        except KeyboardInterrupt:
            print("\nInstallation cancelled.")
            exit()