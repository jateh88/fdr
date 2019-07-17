class Field:

    __value_seq = None  # This will ultimately be a tuple containing the cell values
    __column_number_seq = None
    __header_name_seq = None

    def __init__(self, row_number):
        self.row_number = row_number

    @classmethod
    def get_column_number_seq(cls, header_seq):
        """The returned column numbers determine which cell data will be passed to this object later."""
        # Return None if column not found? Or -1? Or False?
        pass

    @classmethod
    def validate_column_position(cls, previous_column_number):
        # TODO: write this method
        col_num = 42
        return col_num

    @classmethod
    def set_values(cls, values_seq):
        # TODO check that input is a sequence that can be converted to tuple.
        cls.__values_seq = values_seq

    @classmethod
    def validate(cls):
        # This remains empty. The child classes will polymorph this into their own
        pass

    @classmethod
    def __not_empty(cls):
        # loop thru value_seq and check to make sure they're strings not equal to ''
        pass
