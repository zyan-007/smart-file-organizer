import os
import shutil
from utils import get_category, log_action, get_unique_filename, get_file_date
from config import load_config, get_ignore_folders
from history import record_move


def organize_files(path, dry_run=False, recursive=False, min_size=0, by_date=False, enable_log=True):
    if not os.path.exists(path):
        print("Invalid path")
        return

    categories = load_config()
    ignore_folders = get_ignore_folders(categories)

    all_files = []

    # collect files first (for progress)
    for root, dirs, files in os.walk(path):
        if not recursive:
            dirs.clear()

        dirs[:] = [d for d in dirs if d not in ignore_folders]

        for file in files:
            all_files.append((root, file))

    total = len(all_files)
    processed = 0

    print(f"Total files to process: {total}\n")

    for base_path, file in all_files:
        if process_file(base_path, file, categories, dry_run, min_size, by_date, enable_log):
            processed += 1

        print(f"[{processed}/{total}] Processed", end="\r")

    print(f"\n\nCompleted. {processed} files organized.")


def process_file(base_path, file, categories, dry_run, min_size, by_date, enable_log):
    full_path = os.path.join(base_path, file)

    if not os.path.isfile(full_path):
        return False

    if os.path.getsize(full_path) < min_size:
        return False

    category = get_category(file, categories)

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

        message = f"Moved {file} -> {target_dir}"
        print(message)

        if enable_log:
            log_action(message)

        return True

    except Exception as e:
        print(f"Error processing {file}: {e}")
        return False