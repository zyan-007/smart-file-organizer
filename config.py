FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Code": [".py", ".cpp", ".js", ".html", ".css"],
}

IGNORE_FOLDERS = set(FILE_CATEGORIES.keys()) | {"Others"}