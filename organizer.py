import os
import shutil
from utils import get_category, log_action, get_unique_filename, get_file_date
from config import load_config, get_ignore_folders
from history import record_move


def organize_files(path, dry_run=False, recursive=False, min_size=0, by_date=False):
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
                organize_files(full_path, dry_run, recursive, min_size, by_date)
            continue

        if process_file(path, item, categories, dry_run, min_size, by_date):
            count += 1

    print(f"\nProcessed {count} files in: {path}")


def process_file(base_path, file, categories, dry_run, min_size, by_date):
    full_path = os.path.join(base_path, file)

    if not os.path.isfile(full_path):
        return False

    if os.path.getsize(full_path) < min_size:
        return False

    category = get_category(file, categories)

    # date-based structure
    if by_date:
        year, month = get_file_date(full_path)
        target_dir = os.path.join(base_path, category, year, month)
    else:
        target_dir = os.path.join(base_path, category)

    target_path = os.path.join(target_dir, file)

    try:
        if dry_run:
            print(f"[DRY RUN] {file} -> {target_dir}")
            return True

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        target_path = get_unique_filename(target_path)

        shutil.move(full_path, target_path)
        record_move(full_path, target_path)

        print(f"Moved {file} -> {target_dir}")
        log_action(f"Moved {file} -> {target_dir}")

        return True

    except Exception as e:
        print(f"Error processing {file}: {e}")
        return False