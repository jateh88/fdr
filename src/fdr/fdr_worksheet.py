# This is a list of classes, each containing the logic for a worksheet field (or grouping of fields):
import openpyxl
import click
# from .fields import field_class_seq
from fdr.fields import field_class_seq
from collections import namedtuple

WorksheetColumn = namedtuple("WorksheetColumn", "header values")


class FdrWorksheet:

    def __init__(self, path):
        self.path = path  # TODO add check for path string ending in '.xlsx' or '.xls'
        self.worksheet_name = "Procedure Based Requirements"
        ws_column_seq = self._import_worksheet(path, self.worksheet_name)
        # self.field_seq = self._set_fields(ws_column_seq)

    @staticmethod
    def _import_worksheet(path, worksheet_name):
        """Return list of WorksheetColumn namedtuples"""
        # TODO add a check to see if this is a valid path.
        #   Add a try
        # try:
        wb = openpyxl.load_workbook(path)
        # except:
            # raise ValueError(f"{worksheet_name} worksheet not found.")
        # TODO replace valueerror with custom validation error
        # TODO: add extra functionality. If exact worksheet name is not found,
        #   use the most similar one and inform user of this.
        ws = wb[worksheet_name]
        ws_data = []
        start_column_num = 1
        for col in range(start_column_num, ws.max_column + 1):
            header_name = ws.cell(1, col).value
            values_seq = []
            for row in range(2, ws.max_row + 1):
                values_seq.append(ws.cell(row, col).value)
            ws_column = WorksheetColumn(header=header_name, values=values_seq)
            ws_data.append(ws_column)
        return ws_data

    @staticmethod
    def _set_fields(ws_column_seq):


        column_num_cur = 0
        field_seq = [Field() for Field in field_class_seq]
        for field in field_seq:
            field.find_indices(header_name_seq)
            field.validate_column_count()  # TODO this shouldn't be called yet. First, initialize (import), then val.
            column_num_cur = field.validate_column_position(column_num_cur)
            field.set_values(col_values_seq)
        return field_seq

    @staticmethod
    def validate():
        click.echo("Validating...")
