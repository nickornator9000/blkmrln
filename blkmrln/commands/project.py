"""
TODO
This command should be the users go to when looking at their projects. 
1. A flag to list all projects
EX:
project_1
project_2

2. A flag to list all projects with sub grouping of features
EX:
project_1
    -> feature_1
    -> feature_2
project_2
    -> feature_1
    -> feature_2

3. an opt to only list the feature sub groupings of named projects
EX: (Name project_1)
project_1
    -> feature_1
    -> feature_2
project_2

NOTE
This command is meant to show the user their projects not create or 
destroy projects that is soley up to the build command. 
"""
from ..core import Core
class Project(Core):
    pass

def execute(args):
    pass