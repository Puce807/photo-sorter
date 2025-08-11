import tkinter as tk
from tkinter import filedialog

import os

from config import IMAGE_EXTENSIONS


def file_browser(message="Select a directory"):
    root = tk.Tk()
    root.withdraw()
    selected_folder = filedialog.askdirectory(
        title=message
    )
    return selected_folder


def read_source(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            if ext in IMAGE_EXTENSIONS:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    content = f.read()
                    yield file_path, content