import os
from datetime import datetime


def get_category(file_name, categories):
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    for category, extensions in categories.items():
        if ext in extensions:
            return category

    return "Others"


def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("organizer.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def get_unique_filename(path):
    base, ext = os.path.splitext(path)
    counter = 1

    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}({counter}){ext}"
        counter += 1

    return new_path


def get_file_date(file_path):
    timestamp = os.path.getmtime(file_path)
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y"), dt.strftime("%m")