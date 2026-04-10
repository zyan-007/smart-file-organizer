import argparse
from organizer import organize_files
from undo import undo_last_operation


def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")

    parser.add_argument("path", nargs="?", help="Folder path to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    parser.add_argument("--recursive", action="store_true", help="Include subfolders")
    parser.add_argument("--undo", action="store_true", help="Undo last operation")
    parser.add_argument("--min-size", type=int, default=0, help="Minimum file size in bytes")

    args = parser.parse_args()

    if args.undo:
        undo_last_operation()
        return

    if not args.path:
        print("Please provide a path or use --undo")
        return

    organize_files(
        args.path,
        dry_run=args.dry_run,
        recursive=args.recursive,
        min_size=args.min_size
    )


if __name__ == "__main__":
    main()