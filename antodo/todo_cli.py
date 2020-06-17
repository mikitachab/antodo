import contextlib
from typing import List

import click

from .todo import Todos


@click.group()
def todo_cli():
    pass


@todo_cli.command()
def show():
    todos = Todos()
    print_todos(todos)


@todo_cli.command()
@click.argument("content", type=click.STRING)
@click.option("--urgent", "-u", is_flag=True)
def add(content: str, urgent: bool):
    with todos_operation() as todos:
        todos.add_todo(content, urgent)


@todo_cli.command()
@click.argument("indexes", nargs=-1, type=click.INT)
def remove(indexes: List[int]):
    with todos_operation() as todos:
        indexes_to_remove = []
        for index in indexes:
            index_to_remove = index - 1
            if index_to_remove < len(todos):
                indexes_to_remove.append(index_to_remove)
            else:
                click.echo(f"no todo with index {index}")

        todos.remove_todos(indexes_to_remove)
        click.echo(f"deletd todos: {indexes_to_remove}")


@contextlib.contextmanager
def todos_operation():
    todos = Todos()
    yield todos
    print_todos(todos)


def print_todos(todos: Todos):
    if todos:
        for index, todo in enumerate(todos, 1):
            if todo.urgent:
                click.secho(f"{index}. {todo.content}", fg="red")
            else:
                click.echo(f"{index}. {todo.content}")
    else:
        click.echo("No todos found")
