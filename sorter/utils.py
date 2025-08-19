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

def dms_to_decimal(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1]
    seconds = dms[2][0] / dms[2][1]
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal