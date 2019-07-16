import click
from .excel_path import get_new_path_from_dialog


def get_excel_path():
    path = get_new_path_from_dialog()
    # TODO add check for path string ending in '.xlsx' or '.xls'
    return path


def print_basic_report(excel_path):
    click.echo(
        f"Here's the path you selected: {excel_path}\n"
        "This is where we print a basic report..."
    )
