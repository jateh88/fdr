import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def get_new_path_from_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = Path(filedialog.askopenfilename())
    return file_path

