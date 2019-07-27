import click
from collections import namedtuple

WorksheetColumn = namedtuple("WorksheetColumn", "header body")


class Field:

    field_name = None

    def __init__(self, all_worksheet_columns):

        matching_worksheet_columns = [
            (index, ws_col)
            for index, ws_col in enumerate(all_worksheet_columns)
            if ws_col.header.lower() == self.get_field_name().lower()
        ]

        # Defaults:
        self._indices = None  # Used in later check of relative column position
        self._body = None  # column data
        self._correct_position = None

        # Override defaults if matches are found:
        if len(matching_worksheet_columns) >= 1:
            indices, worksheet_columns = zip(*matching_worksheet_columns)
            # Get all matching _indices (used for checking duplicate data and proper sorting)
            self._indices = indices
            # Get first matching column data (any duplicate columns are ignored; user rcv warning)
            self._body = worksheet_columns[0]

    def validate(self):
        self._get_validation_raw_data()
        self._print_validation_report()

    def _get_validation_raw_data(self):
        click.echo(f"Validating the '{self.get_field_name()}' field!")

    def _print_validation_report(self):
        click.echo(f"Generating validation report for the '{self.get_field_name()}' field!")

    def field_found(self):
        if self._body is None:
            return False
        return True

    def _get_index(self):
        return self._indices[0]

    def validate_position(self, previous_index):
        """Check that this field comes after the previous one. Return this column number."""
        if not self.field_found():
            return previous_index
        if self._get_index() > previous_index:
            self._correct_position = True
        else:
            self._correct_position = False
        return self._get_index()

    @classmethod
    def get_field_name(cls):
        return cls.field_name


if __name__ == "__main__":
    from collections import namedtuple

    yarp = namedtuple("WorksheetColumn", "field_name body")
    print(yarp.__name__)
