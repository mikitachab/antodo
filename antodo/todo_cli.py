import click


@click.group()
def todo_cli():
    pass


@todo_cli.command()
@click.argument("content", type=click.STRING)
@click.option("--urgent", "-u", is_flag=True)
def add(content: str, urgent: bool):
    if urgent:
        click.secho(content, fg="red")
    else:
        click.echo(content)
