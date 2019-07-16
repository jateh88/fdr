from .get_path_from_user import get_path_from_user
from .. import __version__
from .workbook import Workbook
import click



@click.command()
@click.option('--version', '-v', is_flag=True)
def main(version):

    if version:
        string_ = 'version: ' + __version__
        click.echo(string_)
        return

    fdr_excel_path = get_path_from_user()

    workbook_ = Workbook()
    workbook_.import_from_excel(fdr_excel_path)
    workbook_.validate_fdr()
    workbook_.validate_core()
