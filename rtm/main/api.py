"""The main() function here defines the structure of the RTM Validation
process. It calls the main steps in order and handles exceptions directly
related to validation errors (e.g. missing columns)"""

# --- Standard Library Imports ------------------------------------------------
# None

# --- Third Party Imports -----------------------------------------------------
import click

# --- Intra-Package Imports ---------------------------------------------------
import rtm.main.excel as excel
from rtm.main.exceptions import RTMValidatorError
from rtm.containers.fields import Fields
import rtm.containers.worksheet_columns as wc
import rtm.containers.work_items as wi
import rtm.main.context_managers as context


def main(highlight_bool=False, highlight_original=False, path=None):
    """This is the main function called by the command line interface."""

    click.clear()
    click.echo(
        "\nWelcome to the DePuy Synthes Requirements Trace Matrix (RTM) Validator."
        "\nPlease select an RTM excel file you wish to validate."
    )

    version_check()

    if highlight_original:
        highlight_original = click.confirm('Are you sure you want to edit the original excel file? Images, etc will be lost.')

    try:
        if not path:
            path = excel.get_rtm_path()
        wb = excel.get_workbook(path)
        ws = excel.get_worksheet(wb, "Procedure Based Requirements")
        worksheet_columns = wc.WorksheetColumns(ws)
        with context.worksheet_columns.set(worksheet_columns):
            fields = Fields()
        with context.fields.set(fields):
            work_items = wi.WorkItems()
        with context.fields.set(fields), context.work_items.set(work_items):
            fields.validate()
            fields.print()
        if highlight_bool:
            excel.mark_up_excel(path, wb, ws, fields.excel_markup, highlight_original)
    except RTMValidatorError as e:
        click.echo(e)

    click.echo(
        "\nThank you for using the RTM Validator."
        "\nIf you have questions or suggestions, please contact a Roebling team member.\n"
    )


def version_check() -> str:
    """Tell user if app is up to date"""

    project_info = pypi_get.get("dps-rtm")
    pypi_version = project_info['info']['version']

    if pypi_version == current_version:
        click.echo(f"\nYour app is up to date ({current_version})")
    else:
        click.secho(
            "\nYour app is out of date.",
            fg='red',
            bold=True,
        )
        click.echo(f"Currently installed: {current_version}")
        click.echo(f"Available: {pypi_version}")
        click.echo("Upgrade to the latest by entering the following:")
        click.echo(f"pip install --upgrade dps-rtm")


if __name__ == "__main__":
    main()
