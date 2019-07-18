from .field import Field
import click


class ID(Field):

    _header_names = ['id']

    def validate(self):
        # - column exists
        # - cells not empty
        # - cells in alphabetical order
        index = 99
        row = self._get_row(index)
        click.echo("Validating ID Field!")

    def starts_with_p(self):
        pass