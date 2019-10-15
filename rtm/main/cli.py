"""This is pretty boiler plate right now. Later, as more command line options
are added in, this module will become more substantial."""

# --- Standard Library Imports ------------------------------------------------
# None

# --- Third Party Imports -----------------------------------------------------
import click

# --- Intra-Package Imports ---------------------------------------------------
from rtm.main import api


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """Type ``rtm`` on the command line to run the RTM Validator.

    Here are some other commands to try:

    ``rtm markup`` to print the RTM Validator results to a copy of your original RTM worksheet.

    ``rtm markup --help`` to see additional options and commands available to the ``rtm markup`` command, such as...

    ``rtm markup --original`` to have the RTM Validator mark up your original RTM file.
    """
    if ctx.invoked_subcommand is None:
        api.main()


@main.command()
@click.option('--original', '-o', is_flag=True, help='Save markup to original file')
def markup(original):
    """Markup a RTM worksheet. Problem cells get highlighted and commented. README tab gives add'l info."""
    api.main(True, original)
