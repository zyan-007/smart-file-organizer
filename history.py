import json
import os

HISTORY_FILE = "history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def record_move(src, dest):
    history = load_history()
    history.append({"src": src, "dest": dest})
    save_history(history)


def clear_history():
    save_history([])