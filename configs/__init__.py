import json
import os

CONFIG_FILE_PATH = "c:/Users/Public/Documents/config.json" if os.name == "nt" else "/.config.json"

DEFAULT_CONFIG = {
    "background_image": None,
}


def load_config() -> dict:
    try:
        with open(CONFIG_FILE_PATH, "r") as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        with open(CONFIG_FILE_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f)
            return DEFAULT_CONFIG


def save_config(key: str, value: str):
    config = load_config()
    config[key] = value
    with open(CONFIG_FILE_PATH, "w") as f:
        json.dump(config, f)
