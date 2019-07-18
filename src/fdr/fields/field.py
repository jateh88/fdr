import click

class FieldNotFound:
    # def __iter__(self):
    #     return
    pass



class Field:
    _header_names = None

    # --- INITIALIZE ----------------------------------------------------------

    def __init__(self, ws_column_seq):
        # TODO do a type check (sequence of WorksheetColumn objects)

        worksheet_headers = tuple(column.header for column in ws_column_seq)
        worksheet_body = tuple(column.values for column in ws_column_seq)

        matching_indices = self.get_matching_indices(worksheet_headers)
        # if not isinstance(matching_indices, NotExist):
        matching_columns = self._get_matching_columns(worksheet_body, matching_indices)

        self._indices = matching_indices
        self._columns = matching_columns

    @classmethod
    def get_matching_indices(cls, worksheet_headers):
        worksheet_headers = [header.lower() for header in worksheet_headers]
        sought_headers = [header.lower() for header in cls._header_names]

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
        click.echo("Validating __ Field!")

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
        return cls._header_names

    def get_indices(self):
        return self._indices

    # --- STATIC METHODS ------------------------------------------------------

    @staticmethod
    def _get_row(index):
        starting_row = 2
        return index + starting_row