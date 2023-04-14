import yaml
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(object):
    """
    A class to manage all configurations.
    """
    def __init__(self):
        self.app_config = AppConfig()
        self.script_config = ScriptConfig()

    def app(self, property_name):
        return self.app_config.get_property(property_name)

    def script(self, property_name):
        return self.script_config.get_property(property_name)

    def __getattr__(self, property_name):
        app_property = self.app(property_name)
        if app_property is not None:
            return app_property
        script_property = self.script(property_name)
        if script_property is not None:
            return script_property

        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{property_name}'")

class AppConfig(object):
    """
    A class to manage app configurations.
    """
    def __init__(self):
        self._config = {
            "debug": False,
            "openai_api_key": os.environ.get("OPENAI_API_KEY"),
            "pexels_api_key": os.environ.get("PEXELS_API_KEY"),
            "shutterstock_api_key": os.environ.get("SHUTTERSTOCK_API_KEY")
        }

    def get_property(self, property_name):
        return self._config.get(property_name)
    
    def set_debug(self, debug):
        self._config["debug"] = debug

    def update_from_args(self, args):
        self.set_debug(args.debug)

    def log_args(self):
        debug = self.get_property("debug")
        print(f"Debug mode: {debug}")
    
class ScriptConfig(object):
    """
    A class to manage script configurations.
    """
    def __init__(self):
        defaults = {
            "script_style": "informative",
            "max_content_length": 200,
            "max_timeline_entries": 3,
            "footage_engine": "pexels",
            "footage_engine_settings": {}
        }
        with open("input/settings.yml", "r") as file:
            input_settings = yaml.safe_load(file) or {}

        input_settings = {**defaults, **input_settings}
        self._config = input_settings

    def get_property(self, property_name):
        return self._config.get(property_name)
