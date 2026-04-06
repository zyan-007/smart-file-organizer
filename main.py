'''main file'''
import argparse
from organizer import organize_files

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")

    parser.add_argument("path", help="Folder path to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    parser.add_argument("--recursive", action="store_true", help="Include subfolders")

    args = parser.parse_args()

    organize_files(
        args.path,
        dry_run=args.dry_run,
        recursive=args.recursive
    )

if __name__ == "__main__":
    main()