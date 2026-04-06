import os
import shutil
from utils import get_category, log_action

IGNORE_FOLDERS = {"Images", "Documents", "Videos", "Audio", "Code", "Others"}


def organize_files(path, dry_run=False, recursive=False):
    if not os.path.exists(path):
        print("Invalid path")
        return

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            if recursive and item not in IGNORE_FOLDERS:
                organize_files(full_path, dry_run, recursive)
            continue

        process_file(path, item, dry_run)


def process_file(base_path, file, dry_run):
    full_path = os.path.join(base_path, file)

    if not os.path.isfile(full_path):
        return

    category = get_category(file)
    target_dir = os.path.join(base_path, category)
    target_path = os.path.join(target_dir, file)

    try:
        if dry_run:
            print(f"[DRY RUN] {file} -> {category}/")
            return

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        if os.path.exists(target_path):
            print(f"Skipping {file}, already exists")
            return

        shutil.move(full_path, target_path)
        print(f"Moved {file} -> {category}/")
        log_action(f"Moved {file} -> {category}/")

    except Exception as e:
        print(f"Error processing {file}: {e}")