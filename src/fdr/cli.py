import click
import fdr


@click.command()
def fdr_cli():
    path = fdr.get_excel_path()
    fdr.print_basic_report(path)
