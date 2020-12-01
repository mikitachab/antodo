from dataclasses import asdict

import click

import antodo


class Todos:
    def __init__(self):
        self._loader = antodo.TodosLoader()
        self._todos: list = self._loader.load_todos()

    def add_todo(self, content: str, urgent: bool):
        self._todos.append(antodo.Todo(content, urgent))

    def remove_todos(self, indexes_to_remove):
        self._todos = [
            todo for index, todo in enumerate(self._todos) if index not in indexes_to_remove
        ]

    def save(self):
        self._loader.save_todos(self)

    def to_json(self):
        return list(map(lambda todo: asdict(todo), self._todos))

    def show(self):
        for index, todo in enumerate(self._todos, 1):
            click.secho(f"{index}. {todo.content}", fg=todo.get_color())
            if todo.subtasks:
                for i, task in enumerate(todo.subtasks):
                    click.echo(f"\t{i+1} {task}")

    def clear(self):
        self._todos = []

    def __getitem__(self, index):
        return self._todos[index]

    def __setitem__(self, index, value):
        self._todos[index] = value

    def __bool__(self):
        return bool(self._todos)

    def __len__(self):
        return len(self._todos)

    def __iter__(self):
        return iter(self._todos)
