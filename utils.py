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


def get_unique_filename(path):
    """
    If file exists, append (1), (2), etc.
    """
    base, ext = os.path.splitext(path)
    counter = 1

    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}({counter}){ext}"
        counter += 1

    return new_path