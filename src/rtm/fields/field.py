import click
from collections import namedtuple

WorksheetColumn = namedtuple("WorksheetColumn", "header values")


class FieldNotFound:
    pass


class Field:
    field_name = None

    # --- INITIALIZE ----------------------------------------------------------

    def __init__(self, all_worksheet_columns):
        if not isinstance(all_worksheet_columns, WorksheetColumn):
            raise TypeError(
                f"You tried initializing the {self.get_field_name()} field "
                f"with something other than a {WorksheetColumn.__name__} object"
            )

        # TODO do a type check (sequence of WorksheetColumn objects)

        worksheet_headers = tuple(column.header for column in all_worksheet_columns)
        worksheet_body = tuple(column.values for column in all_worksheet_columns)

        matching_indices = self.get_matching_indices(worksheet_headers)
        # if not isinstance(matching_indices, NotExist):
        matching_columns = self._get_matching_columns(worksheet_body, matching_indices)

        self._indices = matching_indices
        self._columns = matching_columns

    @classmethod
    def get_field_name(cls):
        return cls.field_name

    @classmethod
    def get_matching_indices(cls, worksheet_headers):
        worksheet_headers = [header.lower() for header in worksheet_headers]
        sought_headers = [header.lower() for header in cls.field_name]

        matching_columns_indices = []
        # TODO check for the existance of field name first.
        field_found = False
        for index, header in enumerate(worksheet_headers):
            if header in sought_headers:
                matching_columns_indices.append(index)
                field_found = True
        if field_found:
            return matching_columns_indices
        else:
            return FieldNotFound()

    @staticmethod
    def _get_matching_columns(worksheet_body, indices):
        # TODO check that input is a sequence that can be converted to tuple.
        if isinstance(indices, FieldNotFound):
            return FieldNotFound()
        matching_columns = [worksheet_body[index] for index in indices]
        return matching_columns

    # --- VALIDATE ------------------------------------------------------------

    def validate(self):
        click.echo(f"Validating the '{self.get_field_name()}' field!")

    @classmethod
    def validate_column_position(cls, previous_column_num):
        """Check that this field comes after the previous one. Return this column number."""
        if isinstance(cls.__column_num_seq, FieldNotFound):
            # This field doesn't exist in excel sheet
            return None
        first_column_num = cls.__column_num_seq[0]
        last_column_num = cls.__column_num_seq[-1]
        if previous_column_num < first_column_num:
            cls.__in_position = True
        else:
            cls.__in_position = False
        return last_column_num

    def validate_field_exists(self):
        pass

    # --- PROPERTIES ----------------------------------------------------------

    @classmethod
    def get_names(cls):
        return cls.field_name

    def get_indices(self):
        return self._indices

    # --- STATIC METHODS ------------------------------------------------------

    @staticmethod
    def _get_row(index):
        starting_row = 2
        return index + starting_row


# if __name__ == "__main__":
#     from collections import namedtuple
#     yarp = namedtuple('WorksheetColumn', 'field_name body')
#     print(yarp.__name__)
