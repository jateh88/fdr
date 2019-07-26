import openpyxl
import click
# from src.rtm.fields import WorksheetColumn, field_classes
from rtm.fields import WorksheetColumn, field_classes
from rtm.exceptions import RTMValidatorFileError


class RTMWorksheet:

    # Initialize each field with its data
    def __init__(self, path):
        worksheet = self._get_worksheet(path, worksheet_name = "Procedure Based Requirements")
        self._fields = self._initialize_fields(field_classes, worksheet)

    @staticmethod
    def _get_worksheet(path, worksheet_name):
        """Return list of WorksheetColumn objects"""

        # --- Get Workbook ----------------------------------------------------
        wb = openpyxl.load_workbook(
            filename=str(path),
            read_only=True,
            data_only=True,
        )

        # --- Get Worksheet ---------------------------------------------------
        ws = None
        for sheetname in wb.sheetnames:
            if sheetname.lower() == worksheet_name.lower():
                ws = wb[sheetname]
        if ws == None:
            raise RTMValidatorFileError(
                f"\nError: The RTM workbook does not contain a '{worksheet_name}' worksheet")

        # --- Convert Worksheet to WorksheetColumn objects --------------------
        ws_data = []
        start_column_num = 1
        for col in range(start_column_num, ws.max_column + 1):
            column_header = ws.cell(1, col).value

            column_body = tuple(
                ws.cell(row, col).value
                for row
                in range(2, ws.max_row + 1))

            # column_body = []
            # for row in range(2, ws.max_row + 1):
            #     column_body.append(ws.cell(row, col).value)

            ws_column = WorksheetColumn(header=column_header, values=column_body)
            ws_data.append(ws_column)

        return ws_data

    @staticmethod
    def _initialize_fields(field_classes, worksheet_columns):
        """Get list of field objects that each contain their portion of the worksheet_columns"""
        return [Field(worksheet_columns) for Field in field_classes]

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


if __name__ == "__main__":
    pass
