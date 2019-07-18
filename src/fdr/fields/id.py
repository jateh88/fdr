from .field import Field
import click


class ID(Field):

    __header_name_seq = ['ID']

    def validate(self):
        # - column exists
        # - cells not empty
        # - cells in alphabetical order
        index = 99
        row = self._get_row(index)

        pass

    def starts_with_p(self):
        pass