from os import listdir, path

def get_node_versions():
    
    def get_node_version_name(name: str): 
        split_name = name.split('v')
        split_name = split_name[1].split('-')
        return split_name[0]
    
    folders = []
    node_dir = path.expanduser('~/node')
    
    # Check if the node directory exists
    if not path.exists(node_dir):
        return []

    for folder in listdir(node_dir):
        if path.isdir(path.expanduser(f"~/node/{folder}")) and folder.startswith("node-v"):
            folders.append(folder)

    versions = []

    for folder in folders:
        versions.append(get_node_version_name(folder))

    return versions

def list_node_versions():
    for version in get_node_versions():
        print(version)