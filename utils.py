import os
from config import FILE_CATEGORIES

def get_category(file_name):
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category

    return "Others"