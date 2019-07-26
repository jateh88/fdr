from .field import Field
import click


class ID(Field):
    field_name = 'id'

    def validate(self):
        click.echo("Validating ID Field!")
