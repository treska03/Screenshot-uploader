import json

from src.main.util.exceptions import CorruptedConfigFileError

class Config_handler:

    @staticmethod
    def _save_to_file(data):
        with open("config.json", "w") as config:
            config.write(json.dumps(data, indent=4))

    @staticmethod
    def _load_file(path="config.json"):
        try:
            with open(path, "r") as f:
                return json.loads(f.read())
        except FileNotFoundError:
            raise FileNotFoundError("config.json does not exist in the main directory")
            
    @staticmethod
    def _get_from_key(key):
        try:
            return Config_handler._load_file()[key]
        except KeyError:
            raise CorruptedConfigFileError(f"Config file incorrectly formatted - {key} key missing")
        
    @staticmethod
    def _set_for_key(key, val):
        config_dict = Config_handler._load_file()
        if not key in config_dict.keys():
            raise CorruptedConfigFileError(f"Config file incorrectly formatted - {key} key missing")
        config_dict[key] = val
        Config_handler._save_to_file(config_dict)
        
    @staticmethod
    def get_shortcuts():
        return set(Config_handler._get_from_key("shortcut_keys"))
    
    @staticmethod
    def get_token():
        return Config_handler._get_from_key("TOKEN")
    
    @staticmethod
    def set_shortcuts(new_shortcuts):
        Config_handler._set_for_key("shortcut_keys", list(set(new_shortcuts)))
    
    @staticmethod
    def set_token(token):
        Config_handler._set_for_key("TOKEN", token)