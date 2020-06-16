import functools
import json

from click.testing import CliRunner
import pytest

from antodo import todo_cli
from antodo import config
from antodo.todo import Todos


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
    with open(todos_path, "w") as file:
        json.dump({"todos": []}, file)
    monkeypatch.setattr(config, "TODOS_JSON_PATH", todos_path)


@pytest.fixture
def add_todo(todos_json_path):
    todos = Todos()

    def _add_todo(content, urgent=False):
        todos.add_todo(content, urgent)

    return _add_todo
