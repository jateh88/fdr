import click
import fdr


@click.command()
def fdr_cli():
    path = fdr.get_excel_path()
    workbook = fdr.get_workbook(path)
    fdr.validate_fdr_workbook(workbook)
