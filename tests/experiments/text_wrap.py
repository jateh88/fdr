import click

lorips = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
         "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"


def printstuff() -> None:
    ruler = '    *    |' * 7
    click.echo(ruler)
    # --- Print Score in Color ------------------------------------------------
    tab_character_width = 8
    click.secho(f"\tPass\t".expandtabs(tab_character_width), fg='green', bold=True, nl=False)
    # --- Print Rule Title ----------------------------------------------------

    title = "This Is Important"
    title = f"{title} - ".upper()

    # # --- Print Explanation (and Rows) ----------------------------------------

    title_indent_len = 2 * tab_character_width
    indent_len = len(f'{title}') + title_indent_len
    initial_indent = ' ' * indent_len
    # click.secho('\t\t\t', nl=False)
    click.secho(f"{title}", bold=True, nl=False)
    max_width = click.get_terminal_size()[0] - 20
    a = click.wrap_text(lorips, width=max_width, initial_indent=initial_indent, subsequent_indent=' '*title_indent_len).strip()
    click.echo(a)


printstuff()
