import click


def get_excel_path():
    return 42


def print_basic_report(excel_path):
    click.echo(
        f"Here's the dummy path: {excel_path}\n"
        "This is where we print a basic report..."
    )
