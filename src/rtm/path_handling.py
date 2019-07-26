import tkinter as tk
from tkinter import filedialog
from pathlib import Path
# from .exceptions import RTMValidatorError, RTMValidatorFileError
import click


def get_rtm_path():
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


def get_new_path_from_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = Path(filedialog.askopenfilename())
    return file_path


# try:
#     get_rtm_path()
# except RTMValidatorError as e:
#     print(e)
