from ..core import Core
from ..utils import Singleton
class ProjectTestState(Core):
    pass

class FeatureTestState(ProjectTestState):
    pass

class TestState(ProjectTestState,
                FeatureTestState,
                metaclass=Singleton):
    pass

def run_tests():
    pass

def execute(args):
    pass