# This is a list of classes, each containing the logic for a worksheet field (or grouping of fields):
import openpyxl
import click
# from .fields import field_class_seq
from fdr.fields import field_class_seq as field_classes
from collections import namedtuple

WorksheetColumn = namedtuple("WorksheetColumn", "header values")
# TODO: refactor 'values' field to 'body'


class FdrWorksheet:

    def __init__(self, path):
        self.path = path  # TODO add check for path string ending in '.xlsx' or '.xls'
        self.worksheet_name = "Procedure Based Requirements"
        worksheet = self._get_worksheet(path, self.worksheet_name)
        self._fields = self._initialize_fields(field_classes, worksheet)

    @staticmethod
    def _get_worksheet(path, worksheet_name):
        """Return list of WorksheetColumn objects"""
        # TODO add a check to see if this is a valid path.
        #   Add a try
        # try:
        wb = openpyxl.load_workbook(
            filename=path,
            read_only=True,
            data_only=True,
        )
        # except:
            # raise ValueError(f"{worksheet_name} worksheet not found.")
        # TODO replace valueerror with custom validation error
        # TODO: add extra functionality. If exact worksheet name is not found,
        #   use the most similar one and inform user of this.
        worksheet_names = [name.lower() for name in wb.sheetnames]

        try:
            worksheet_index = worksheet_names.index(worksheet_name.lower())
        except ValueError:
            raise ValueError(f"Excel Sheet must contain a '{worksheet_name}' worksheet")
        worksheet_name = wb.sheetnames[worksheet_index]
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
    def _initialize_fields(field_classes, worksheet):
        """Get list of field objects that each contain their portion of the worksheet"""
        return [Field(worksheet) for Field in field_classes]

    def validate(self):
        """Validate each field (e.g. 'ID', 'Devices')"""

        for field in self._fields:
            field.validate()


    # --- PROPERTIES ----------------------------------------------------------

    @property
    def fields(self):
        return self._fields
