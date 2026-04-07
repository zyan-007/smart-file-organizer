import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Code": [".py", ".cpp", ".js", ".html", ".css"],
}


def create_default_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(DEFAULT_CATEGORIES, f, indent=4)


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print("Config not found. Creating default config.json...")
        create_default_config()

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def get_ignore_folders(categories):
    return set(categories.keys()) | {"Others"}