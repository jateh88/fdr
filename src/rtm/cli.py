import click
import rtm


@click.command()
def rtm_cli():
    rtm.validate()
