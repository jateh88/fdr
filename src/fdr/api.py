import click
from .path_handling import get_new_path_from_dialog
from .fdr_worksheet import FdrWorksheet


def validate():
    click.echo("Start App")
    path = get_new_path_from_dialog()
    worksheet = FdrWorksheet(path)
    worksheet.validate()
    click.echo("End App")


if __name__ == "__main__":
    validate()
