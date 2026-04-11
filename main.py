import argparse
from organizer import organize_files
from undo import undo_last_operation


def parse_extensions(ext_list):
    if not ext_list:
        return None
    return [ext.lower() if ext.startswith('.') else f".{ext.lower()}" for ext in ext_list]


def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")

    parser.add_argument("path", nargs="?", help="Folder path to organize")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--undo", action="store_true")
    parser.add_argument("--min-size", type=int, default=0)
    parser.add_argument("--by-date", action="store_true")
    parser.add_argument("--no-log", action="store_true")

    parser.add_argument("--include", nargs="+", help="Only include these extensions")
    parser.add_argument("--exclude", nargs="+", help="Exclude these extensions")
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    if args.undo:
        undo_last_operation()
        return

    if not args.path:
        print("Please provide a path or use --undo")
        return

    include_ext = parse_extensions(args.include)
    exclude_ext = parse_extensions(args.exclude)

    organize_files(
        args.path,
        dry_run=args.dry_run,
        recursive=args.recursive,
        min_size=args.min_size,
        by_date=args.by_date,
        enable_log=not args.no_log,
        include_ext=include_ext,
        exclude_ext=exclude_ext,
        verbose=args.verbose
    )


if __name__ == "__main__":
    main()