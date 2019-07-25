import click
from .path_handling import get_rtm_path
from .fdr_worksheet import FdrWorksheet
from fdr.exceptions import RTMValidatorError
import time


def validate():

    click.echo(
        "\nWelcome to the DePuy Synthes Requirements Trace Matrix (RTM) Validator."
        "\nPlease select an RTM excel file you wish to validate."
    )

    time.sleep(2)
    try:
        path = get_rtm_path()
        worksheet = FdrWorksheet(path)
        worksheet.validate()
    except RTMValidatorError as e:
        click.echo(e)

    click.echo(
        "\nThank you for using the RTM Validator."
        "\nIf you have questions or suggestions, please contact a Roebling team member."
    )
