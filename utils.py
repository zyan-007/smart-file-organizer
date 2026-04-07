import os

def get_category(file_name, categories):
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    for category, extensions in categories.items():
        if ext in extensions:
            return category

    return "Others"


def log_action(message):
    with open("organizer.log", "a") as f:
        f.write(message + "\n")