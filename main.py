import argparse
from organizer import organize_files

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("path", help="Folder path to organize")

    args = parser.parse_args()

    organize_files(args.path)

if __name__ == "__main__":
    main()