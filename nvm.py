from sys import argv
from list import list_node_versions, get_node_versions
from use import use_node_version, read_nvmrc
from install import install_node_version
from remove import remove_node_version
from help import show_help
from available import show_available_versions
from os import path

def auto_nvmrc():
    """Automatically detect and switch to .nvmrc version"""
    version_from_nvmrc = read_nvmrc()
    if version_from_nvmrc:
        if get_node_versions().count(version_from_nvmrc) != 0:
            with open(path.expanduser("~/node/current_used_version"), "w") as f:
                f.write(version_from_nvmrc)
            print(f"Switched to Node.js v{version_from_nvmrc} (from .nvmrc)")
        else:
            print(f"Found .nvmrc with version {version_from_nvmrc}, but it's not installed.")
            print(f"Install it with: nvm install {version_from_nvmrc}")
    # If no .nvmrc found, do nothing (silent)

def main():
    if (len(argv) > 1):
        match argv[1]:
            case ('list' | '-l'):
                list_node_versions()   
            case ('use' | '-u'):
                use_node_version()
            case ('install' | '-i'):
                install_node_version()
            case ('remove' | '-r'):
                remove_node_version()
            case ('help' | '-h'):
                show_help()
            case ('available' | '-a'):
                show_available_versions()
            case ('auto'):
                auto_nvmrc()
            case _:
                print(f"Command '{argv[1]}' not found. Use nvm help or nvm -h to show help.")
    else:
        show_help()

main()
