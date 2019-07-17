import click
from .excel_handling import get_new_path_from_dialog, get_excel_worksheet_data
from .fields import field_seq


def validate():
    click.echo("Start App")
    path = get_new_path_from_dialog()  # TODO add check for path string ending in '.xlsx' or '.xls'
    worksheet_data =get_worksheet_data(path)
    validate_fdr_workbook(worksheet_data)
    click.echo("End App")


def get_worksheet_data(workbook_path):
    # TODO extract the fdr workbook from the excelfile and return it
    worksheet_name = 'Procedure Based Requirements'
    worksheet_data = get_excel_worksheet_data(workbook_path, worksheet_name)
    return worksheet_data


def validate_fdr_workbook(worksheet_data):
    headers_seq = []  # TODO get all the headers from the workbook
    # TODO
    #   get start col
    #   get end   col
    #

    # TODO Dummy header sequence to be replace later with the real thing (should be a tuple):
    start_column_num = 1  # This is a dummy val. Must pull from excel instead.
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

    # --- HEADERS -------------------------------------------------------------
    column_num_cur = 0
    for field in field_seq:
        field.find_column(headers_seq, start_column_num)
        field.validate_column_count()
        column_num_cur = field.validate_column_position(column_num_cur)

    # --- VALUES --------------------------------------------------------------
    pass

def