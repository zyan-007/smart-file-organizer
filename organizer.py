import os
import shutil
from utils import get_category, log_action, get_unique_filename, get_file_date
from config import load_config, get_ignore_folders
from history import record_move


def organize_files(
    path,
    dry_run=False,
    recursive=False,
    min_size=0,
    by_date=False,
    enable_log=True,
    include_ext=None,
    exclude_ext=None,
    verbose=False
):
    if not os.path.exists(path):
        print("Invalid path")
        return

    categories = load_config()
    ignore_folders = get_ignore_folders(categories)

    all_files = []

    for root, dirs, files in os.walk(path):
        if not recursive:
            dirs.clear()

        dirs[:] = [d for d in dirs if d not in ignore_folders]

        for file in files:
            all_files.append((root, file))

    total = len(all_files)
    processed = 0
    skipped = 0

    print(f"Total files found: {total}\n")

    for base_path, file in all_files:
        result = process_file(
            base_path,
            file,
            categories,
            dry_run,
            min_size,
            by_date,
            enable_log,
            include_ext,
            exclude_ext,
            verbose
        )

        if result:
            processed += 1
        else:
            skipped += 1

        print(f"[{processed}/{total}] Processed", end="\r")

    print("\n\nSummary:")
    print(f"Processed: {processed}")
    print(f"Skipped:   {skipped}")
    print(f"Total:     {total}")


def process_file(
    base_path,
    file,
    categories,
    dry_run,
    min_size,
    by_date,
    enable_log,
    include_ext,
    exclude_ext,
    verbose
):
    full_path = os.path.join(base_path, file)

    if not os.path.isfile(full_path):
        return False

    _, ext = os.path.splitext(file)
    ext = ext.lower()

    # include filter
    if include_ext and ext not in include_ext:
        if verbose:
            print(f"Skipping {file} (not in include list)")
        return False

    # exclude filter
    if exclude_ext and ext in exclude_ext:
        if verbose:
            print(f"Skipping {file} (excluded)")
        return False

    # size filter
    if os.path.getsize(full_path) < min_size:
        if verbose:
            print(f"Skipping {file} (too small)")
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

        if verbose:
            print(message)

        if enable_log:
            log_action(message)

        return True

    except Exception as e:
        print(f"Error processing {file}: {e}")
        return False