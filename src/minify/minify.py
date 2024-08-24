from blkmrln.core import Core
import os


class MinifiedBuild(Core):
    def __init__(self,project_name,base_dir=os.getcwd(),env_dir=os.getcwd()):
        super().__init__(project_name,base_dir,env_dir)
        self.import_tree = {}
        #self.minified_build = open('minified.py')
    
    def __del__(self):
        #self.minified_build.close()
        self.__delattr__('import_tree')

    def __enter__(self):
        super().__enter__()
        self.build_import_tree()
        self.parse_import_tree()
        return self

    def build_import_tree(self):
        """
        Starting at the __main__.py of the package iterate through all imports building
        a tree of filepaths where each node represents the filepath to a file required
        for the package build. 
        NOTE The underlying assumption here is that the user will build their package
        structure such that the __main__.py is the entrypoint for the package and all
        imports for the package can be resolved from __main__.py or once of the modules
        imported into it or from one of the modules imported from one of that modules 
        sub modules, etc.. you can see how a tree becomes a natural solution. 
        """
        pass

    def parse_import_tree(self):
        """
        This function will traverse the tree built from build_import_tree() and will run
        parse_node_file() at each node. The final exit case for this function should close
        the file minified.py, not the destructor. The destructor is here as a place holder
        until this is implemented. 
        """
        pass

    def parse_node_file(self):
        """
        This function will only be called by parse_import_tree() and will be used to 
        parse the file associated with the file path provided from the tree node. At 
        each function call this function will parse the tree node file, and write the
        results to self.minified_build. 
        """
        pass