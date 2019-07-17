class Field:

    __value_seq = None  # This will ultimately be a tuple containing the cell values

    def __init__(self, row_number):
        self.row_number = row_number

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
