class NotExist:
    pass


class Field:
    __value_seq = None  # This will ultimately be a tuple containing the cell values
    __column_num_seq = None
    __header_name_seq = None
    __header_name = None
    __in_position = None
    __column_count_should = None

    def __init__(self, row_number):
        self.row_number = row_number

    # --- HEADERS AND COLUMNS -------------------------------------------------

    @classmethod
    def find_column(cls, header_seq, start_column_num):
        column_num_seq = []
        for column_num, header in enumerate(header_seq, start_column_num):
            if cls.__header_name == header:
                column_num_seq.append(column_num)
        if len(column_num_seq):
            cls.__column_num_seq = column_num_seq
        else:
            cls.__column_num_seq = NotExist()

    @classmethod
    def validate_column_position(cls, previous_column_num):
        """Check that this field comes after the previous one. Return this column number."""
        if isinstance(cls.__column_num_seq, NotExist):
            # This field doesn't exist in excel sheet
            return None
        first_column_num = cls.__column_num_seq[0]
        last_column_num = cls.__column_num_seq[-1]
        if previous_column_num < first_column_num:
            cls.__in_position = True
        else:
            cls.__in_position = False
        return last_column_num

    @classmethod
    def validate_column_count(cls):

        pass

    # --- VALUES --------------------------------------------------------------

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
