import click
from .excel_path import get_new_path_from_dialog
from .fields import field_seq



def get_excel_path():
    path = get_new_path_from_dialog()
    # TODO add check for path string ending in '.xlsx' or '.xls'
    click.echo(f"Here's the path you selected: {excel_path}")
    return path


def get_workbook(excel_path):
    # TODO extract the fdr workbook from the excelfile and return it
    workbook = None
    return workbook


def validate_fdr_workbook(workbook):

    click.echo("This is where we print a basic report...")
    headers_seq = [] # TODO get all the headers from the workbook

    for field in field_seq:
        field.calc_column_num(headers_seq)

    previous_column_number = 0
    for field in field_seq:
        previous_column_number = field.validate_column_position(previous_column_number)

