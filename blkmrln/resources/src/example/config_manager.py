from common.app.config_manager_base import BaseConfigManager

class ConfigManager(BaseConfigManager):
    _instance = None

    def __new__(cls,
                logger,
                secrets,
                env_configs,
                *args,
                **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self,
                 logging_enabled:bool,
                 local:bool,
                 config_path:str|None):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.logger = self.get_logger(enabled=logging_enabled)
            self.secrets = self.get_config(config_path=config_path)
            self.env_configs = self.get_env_config()
            self.db_cxn = self.get_db_cxn(local=local)

    def get_db_cxn(self, local=True, **kwargs):
        """
        Morty (You): Ahh jeez Rick I didn't realize you could 
        override the method so easily
        Rick: Ooof*burp*fff courssee you cann MooRRRTTYY don't
        be an id*burp*iootttt
        """
        super().get_db_cxn(local, **kwargs)
        if local==False:
            user = self._configuration['db']['user']
            db_pass = self._configuration['db']['pass']
        return None