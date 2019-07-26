import click
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from rtm.exceptions import RTMValidatorError, RTMValidatorFileError


def get_rtm_path() -> Path:
    path = get_new_path_from_dialog()
    required_extensions = '.xlsx .xls'.split()
    if str(path) == '.':
        raise RTMValidatorFileError("\nError: You didn't select a file")
    if path.suffix not in required_extensions:
        raise RTMValidatorFileError(
            f"\nError: You didn't select a file with "
            f"a proper extension: {required_extensions}"
        )
    click.echo(f"\nThe RTM you selected is {path}")
    return path

def get_new_path_from_dialog() -> Path:
    root = tk.Tk()
    root.withdraw()
    path = Path(filedialog.askopenfilename())
    return path

if __name__ == "__main__":
    try:
        get_rtm_path()
    except RTMValidatorError as e:
        print(e)
