import os

def safe_load_env_var(key):
    value = os.getenv(key)
    if value is None:
        raise Exception(f"Environment variable {key} is not set")
    return value

config = {
    "debug": False,
    "OPENAI_API_KEY": safe_load_env_var("OPENAI_API_KEY"),
    "PEXELS_API_KEY": safe_load_env_var("PEXELS_API_KEY"),
    "SHUTTERSTOCK_API_KEY": safe_load_env_var("SHUTTERSTOCK_API_KEY"),
    "script": {
        "style": "informative",
        "max_content_length": 200,
        "max_timeline_entries": 3
    },
    "footage": {
        "engine": "pexels",
    }
}
