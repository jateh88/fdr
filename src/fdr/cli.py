import click
import fdr


@click.command()
def fdr_cli():
    fdr.validate()
