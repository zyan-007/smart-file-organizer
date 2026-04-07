import os
import shutil
from history import load_history, clear_history


def undo_last_operation():
    history = load_history()

    if not history:
        print("No operations to undo.")
        return

    # reverse order (important)
    for entry in reversed(history):
        src = entry["src"]
        dest = entry["dest"]

        if os.path.exists(dest):
            try:
                shutil.move(dest, src)
                print(f"Restored {dest} -> {src}")
            except Exception as e:
                print(f"Error restoring {dest}: {e}")

    clear_history()
    print("\nUndo completed.")