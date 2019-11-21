"""The main() function here defines the structure of the RTM Validation
process. It calls the main steps in order and handles exceptions directly
related to validation errors (e.g. missing columns)"""

# --- Standard Library Imports ------------------------------------------------
# None

# --- Third Party Imports -----------------------------------------------------
import click
from fuzzytable import FuzzyTable, exceptions as fuzz_e

# --- Intra-Package Imports ---------------------------------------------------
import rtm.main.excel as excel
from rtm.main.exceptions import RTMValidatorError
from rtm.containers.fields import Fields
import rtm.containers.worksheet_columns as wc
import rtm.containers.work_items as wi
import rtm.main.context_managers as context
from rtm.main.versions import print_version_check_message


def main(highlight_bool=False, highlight_original=False, path=None):
    """This is the main function called by the command line interface."""

    click.clear()
    click.echo(
        "\nWelcome to the DePuy Synthes Requirements Trace Matrix (RTM) Validator."
        "\nPlease select an RTM excel file you wish to validate."
    )

    click.echo()
    print_version_check_message()

    if highlight_original:
        highlight_original = click.confirm('Are you sure you want to edit the original excel file? Images, etc will be lost.')

    try:
        excel_path = path if path else excel.get_rtm_path()
        ft = FuzzyTable(
            path=excel_path,
            sheetname="Procedure-Based Requirements",
            # TODO need to create fields list:
            fields=fields,
            header_row_seek=True,
            header_row=20,
            name='rtm'
        )
        # TODO add fuzzytable to requires
        with context.worksheet_columns.set(worksheet_columns):
            fields = Fields()
        with context.fields.set(fields):
            work_items = wi.WorkItems()
        with context.fields.set(fields), context.work_items.set(work_items):
            fields.validate()
            fields.print()
        if highlight_bool:
            excel.mark_up_excel(excel_path, wb, ws, fields.excel_markup, highlight_original)
    except RTMValidatorError as e:
        click.echo(e)
    except fuzz_e.SheetnameError as e:
        # TODO make this specific to rtm
        click.echo(e)

    click.echo(
        "\nThank you for using the RTM Validator."
        "\nIf you have questions or suggestions, please contact a Roebling team member.\n"
    )


if __name__ == "__main__":
    main()
