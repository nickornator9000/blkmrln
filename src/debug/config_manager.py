from common.app.config_manager_base import Singleton, BaseConfigManager

class ConfigManager(BaseConfigManager):
    __metaclass__=Singleton
    
    def __init__(self,
                 logging_enabled:bool,
                 local:bool,
                 config_path:str|None):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.logger = self.get_logger(enabled=logging_enabled)
            self.secrets = self.get_config(config_path=config_path)