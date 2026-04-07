import os
import shutil
from utils import get_category, log_action
from config import load_config, get_ignore_folders
from history import record_move


def organize_files(path, dry_run=False, recursive=False):
    if not os.path.exists(path):
        print("Invalid path")
        return

    categories = load_config()
    ignore_folders = get_ignore_folders(categories)

    count = 0

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            if recursive and item not in ignore_folders:
                organize_files(full_path, dry_run, recursive)
            continue

        if process_file(path, item, categories, dry_run):
            count += 1

    print(f"\nProcessed {count} files in: {path}")


def process_file(base_path, file, categories, dry_run):
    full_path = os.path.join(base_path, file)

    if not os.path.isfile(full_path):
        return False

    category = get_category(file, categories)
    target_dir = os.path.join(base_path, category)
    target_path = os.path.join(target_dir, file)

    try:
        if dry_run:
            print(f"[DRY RUN] {file} -> {category}/")
            return True

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        if os.path.exists(target_path):
            print(f"Skipping {file}, already exists")
            return False

        shutil.move(full_path, target_path)

        # record move for undo
        record_move(full_path, target_path)

        print(f"Moved {file} -> {category}/")
        log_action(f"Moved {file} -> {category}/")

        return True

    except Exception as e:
        print(f"Error processing {file}: {e}")
        return False