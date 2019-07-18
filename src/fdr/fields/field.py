class NotExist:
    pass


class Field:
    __value_seq = None  # This will ultimately be a tuple containing the cell values
    __header_name_seq = None
    __header_name = None
    __in_position = None
    __column_count_should = None

    def __init__(self, ws_column_seq):
        # TODO do a type check (sequence of WorksheetColumn objects)

        header_name_seq = tuple(column.header for column in ws_column_seq)
        col_values_seq = tuple(column.values for column in ws_column_seq)
        self.__index_seq = self.find_indices(header_name_seq)
        self.__value_seq = self.set_values(col_values_seq, self.__index_seq)

    @classmethod
    def find_indices(cls, header_name_seq):
        index_seq = []
        # TODO check for the existance of field name first.
        for index, header in enumerate(header_name_seq):
            if header in cls.__header_name_seq:
                index_seq.append(index)
        if len(index_seq) >= 1:
            return index_seq
        else:
            return NotExist()

    @property
    def indices(self):
        return self.__index_seq

    @staticmethod
    def set_values(column_values_seq, index_seq):
        # TODO check that input is a sequence that can be converted to tuple.
        value_seq = []
        for index in index_seq:
            column_values = column_values_seq[index]
            value_seq.append(column_values)
        return value_seq

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

    @classmethod
    def validate(cls):
        # This remains empty. The child classes will polymorph this into their own
        pass

    @classmethod
    def __not_empty(cls):
        # loop thru value_seq and check to make sure they're strings not equal to ''
        pass

    @staticmethod
    def _get_row(index):
        starting_row = 2
        return index + starting_row