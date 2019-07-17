import click
from .excel_path import get_new_path_from_dialog
from .fields import field_seq



def get_excel_path():
    path = get_new_path_from_dialog()
    # TODO add check for path string ending in '.xlsx' or '.xls'
    click.echo(f"Here's the path you selected: {path}")
    return path


def get_workbook(excel_path):
    # TODO extract the fdr workbook from the excelfile and return it
    workbook = None
    return workbook


def validate_fdr_workbook(workbook):

    click.echo("This is where we print a basic report...")
    headers_seq = [] # TODO get all the headers from the workbook

    # TODO Dummy header sequence to be replace later with the real thing (sould be a tuple):
    headers_seq = {
        '',
        'ID',
        'Procedure Step',
        'User Need',
        'Design Input',
        'DO Solution L1',
        'DO Solution L2',
        'DO Solution L3',
        '',
        'Devices'
    }

    column_num_cur = 0
    for field in field_seq:
        field.find_column(headers_seq)
        column_num_cur = field.validate_column_position(column_num_cur)
