import click
from .path_handling import get_new_path_from_dialog
from .fdr_worksheet import FdrWorksheet
import time


def validate():
    click.echo(
        "\nWelcome to the DePuy Synthes Requirements Trace Matrix (RTM) Validator."
        "\nPlease select an RTM excel file you wish to validate."
        "\nNote: the file must have a .xlsx or .xls extension."
    )

    time.sleep(2)
    path = get_new_path_from_dialog()
    click.echo(f"\nExcel file: {path}")
    worksheet = FdrWorksheet(path)
    worksheet.validate()

    click.echo(
        "\nThank you for using the RTM Validator."
        "\nIf you have questions or suggestions, please contact a Roebling team member."
    )
