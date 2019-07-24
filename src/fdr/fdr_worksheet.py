# This is a list of classes, each containing the logic for a worksheet field (or grouping of fields):
import openpyxl
import click
# from .fields import field_class_seq
from fdr.fields import field_class_seq as field_classes
from collections import namedtuple
from pathlib import Path
from openpyxl.utils.exceptions import InvalidFileException

WorksheetColumn = namedtuple("WorksheetColumn", "header values")


class FdrWorksheet:

    # Initialize each field with its data
    def __init__(self, path):
        self._import_successful = False
        self.path = path
        self.worksheet_name = "Procedure Based Requirements"
        try:
            if path == '.':
                raise ValueError
            worksheet = self._get_worksheet(path, self.worksheet_name)
            self._fields = self._initialize_fields(field_classes, worksheet)
            self._import_successful = True
        except ValueError:
            click.echo("Error: No file selected")
        except InvalidFileException as e:
            click.echo(e)


    @staticmethod
    def _get_worksheet(path, worksheet_name):
        """Return list of WorksheetColumn objects"""
        wb = openpyxl.load_workbook(
            filename=path,
            read_only=True,
            data_only=True,
        )
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
        if self._import_successful:
            for field in self._fields:
                field.validate()
        else:
            click.echo("Import was unsuccessful, so there wasn't anything to validate.")

    # --- PROPERTIES ----------------------------------------------------------

    @property
    def fields(self):
        return self._fields
