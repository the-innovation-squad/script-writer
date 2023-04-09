import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class Singleton(type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self):
        self.debug = False
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.pexels_api_key = os.getenv("PEXELS_API_KEY")

    def set_debug(self, debug):
        self.debug = debug

    def update_from_args(self, args):
        self.set_debug(args.debug)

    def log_args(self):
        print(f"Debug mode: {self.debug}")