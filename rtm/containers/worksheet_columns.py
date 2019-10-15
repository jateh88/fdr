"""This module defines the worksheet column class and the custom sequence
containing all the worksheet columns. Worksheet columns are containers housing
a single column from a worksheet."""

# --- Standard Library Imports ------------------------------------------------
from collections import namedtuple
from typing import List

# --- Third Party Imports -----------------------------------------------------
# None

# --- Intra-Package Imports ---------------------------------------------------
from rtm.main.exceptions import RTMValidatorError


WorksheetInfo = namedtuple('WorksheetInfo', 'header_row max_row max_col height')


WorksheetColumn = namedtuple("WorksheetColumn", "header values position column worksheet_info")
# header: row 1
# values: list of cell values starting at row 2
# position: similar to column number, but starts as zero, like an index
# column: column number (start at 1)


class WorksheetColumns:

    def __init__(self, worksheet):

        # --- Attributes ------------------------------------------------------
        max_row = worksheet.max_row
        header_row = get_header_row(worksheet)
        max_col = worksheet.max_column
        self.worksheet_info = WorksheetInfo(
            header_row=header_row,
            max_row=max_row,
            max_col=max_col,
            height=max_row - header_row,
        )
        self._worksheet_columns = []

        # --- Convert Worksheet to WorksheetColumn objects --------------------
        for position in range(max_col):
            col = position + 1
            header_val = worksheet.cell(header_row, col).value
            column_header = str(header_val)
            column_values = tuple(
                worksheet.cell(row, col).value
                for row in range(header_row+1, max_row + 1)
            )
            ws_column = WorksheetColumn(
                header=column_header,
                values=column_values,
                position=position,
                column=col,
                worksheet_info=self.worksheet_info
            )
            self._worksheet_columns.append(ws_column)

    def get_first(self, header_name):
        """returns the first worksheet_column that matches the header"""
        matches = get_matching_worksheet_columns(self, header_name)
        if len(matches) > 0:
            return matches[0]
        else:
            return None

    # --- Sequence ------------------------------------------------------------
    def __getitem__(self, index):
        return self._worksheet_columns[index]

    def __len__(self):
        return len(self._worksheet_columns)


def get_matching_worksheet_columns(sequence_worksheet_columns, field_name) -> List[WorksheetColumn]:
    """Called by constructor to get matching WorksheetColumn objects"""
    matching_worksheet_columns = [
        ws_col
        for ws_col in sequence_worksheet_columns
        if ws_col.header.lower() == field_name.lower()
    ]
    return matching_worksheet_columns


def get_header_row(worksheet):
    """Return row number of first row to contain case-insensitive 'id' in the first 30 columns."""
    seeking_value = 'ID'
    for row in range(1, 31):
        for col in range(1, 31):
            val = worksheet.cell(row, col).value
            if isinstance(val, str) and val.lower() == seeking_value.lower():
                return row
    raise RTMValidatorError("Header 'ID' not found.")
