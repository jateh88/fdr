from .get_path_from_user import get_path_from_user
from .. import __version__
import click


@click.command()
@click.option('--version', '-v', is_flag=True)
def main(version):

    if version:
        string_ = 'version: ' + __version__
        click.echo(string_)
        return

    fdr_excel_path = get_path_from_user()
    print("Here is the path to the file you selected:", fdr_excel_path)
