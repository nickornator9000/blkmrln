import os
from ..utils import copy_directory_contents
from ..core import Core
import importlib.resources

def get_resources_directory():
    """
    Get the path to the `resources` directory within the `my_tool` package.
    """
    resources_path = importlib.resources.files('blkmrln').joinpath('resources')
    
    return str(resources_path)

def execute(args):
    project_name = args.name
    if project_name == None:
        project_name = 'example'
    print(f"Building Project: {project_name}")
    target_root = os.path.join(os.getcwd(), project_name)
    print(f"ROOT DIR = {target_root}")
    pm = Core(project_name=project_name,base_dir=os.getcwd())
    pm.setup_project_structure()
    
    source_dir = get_resources_directory()
    print(f"Setting up project directories in {target_root}")
    copy_directory_contents(source_dir, target_root)

    print(f"Copying {project_name} Build files to {target_root}")