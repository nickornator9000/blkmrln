"""
TODO
This command should control black formatting for the repository and should 
be built to:
1. Format the entire project
2. Format a subfolder of the project. 
3. Show formatted and unformatted code by:
    a. Project
    b. Feature
NOTE
The default project selection should be the current directory IF the current
directory is a project directory. Otherwise this command should require the 
user to provide a project name via opt. 
"""
from ..core import Core

class Format(Core):
    pass

class FormatProject(Format):
    pass

class FormatFeature(FormatProject):
    pass

def run_formatter():
    pass

def execute(args):
    pass