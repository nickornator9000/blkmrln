"""
TODO
This command should be the central location where a user can interact with 
their virtual environments. 
1. User should be able to list all virtual environments and virtual environments
must be linked to /dep/common/requirements.txt for their associated project. 
EX:
venvs/projects
    -> project_1
        -| distlib==0.3.8
        -| filelock==3.15.4
        -| iniconfig==2.0.0
    -> project_2
        -| pytest==8.3.2
        -| pytest-mock==3.14.0
        -| PyYAML==6.0.2
2. User should be able to seamlessly switch between virtual environments 
by providing the project name via an opt to venvmanager. 
3. Initial setup flag with mandatory opt to define a directory outside of project 
directories for storing virtual environments. 
NOTE
This command should not handle the creation and destruction of virtual environments
as that should be heavily linked to the build step, and possibly handled in the 
/resources directory. 
"""