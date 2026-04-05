import os
import shutil
from utils import get_category

def organize_files(path):
    if not os.path.exists(path):
        print("Invalid path")
        return

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            category = get_category(file)
            target_dir = os.path.join(path, category)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            target_path = os.path.join(target_dir, file)

            shutil.move(full_path, target_path)
            print(f"Moved {file} -> {category}/")