import functools
import json

from click.testing import CliRunner
import pytest

import antodo
from antodo import todo_cli
from antodo.todos import Todos


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def todo():
    return todo_cli


@pytest.fixture
def todo_invoke(cli_runner, todo):
    return functools.partial(cli_runner.invoke, todo)


@pytest.fixture(autouse=True)
def todos_json_path(monkeypatch, tmp_path):
    todos_path = str(tmp_path / "todos.json")
    monkeypatch.setattr(antodo.config, "TODOS_JSON_PATH", todos_path)


@pytest.fixture
def add_todo(todos_json_path):
    def _add_todo(content, urgent=False):
        todos = Todos()
        todos.add_todo(content, urgent)
        todos.save()

    return _add_todo


@pytest.fixture
def get_todos(todos_json_path):
    def _make_todos():
        return Todos()

    return _make_todos
