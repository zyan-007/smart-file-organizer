import os
from config import FILE_CATEGORIES

def get_category(file_name):
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category

    return "Others"

def log_action(message):
    with open("organizer.log", "a") as f:
        f.write(message + "\n")