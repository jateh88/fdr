"""This is pretty boiler plate right now. Later, as more command line options
are added in, this module will become more substantial."""

# --- Standard Library Imports ------------------------------------------------
# None

# --- Third Party Imports -----------------------------------------------------
import click

# --- Intra-Package Imports ---------------------------------------------------
from rtm.main import api


@click.command()
@click.option('-V', '--version', is_flag=True, help="Show version and exit.")
def main(version):
    """RTM Validator checks your RTM worksheet for common errors."""
    api.main(version=version)
