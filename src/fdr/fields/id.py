from .field import Field


class ID(Field):

    __header_name_seq = ['ID']

    def validate(self):
        # - column exists
        # - cells not empty
        # - cells in alphabetical order
        pass

