from antodo import __version__


def test_version():
    assert __version__ == "0.2.1"


def test_list_empty_todos(todo_invoke):
    result = todo_invoke(["show"])

    assert result.exit_code == 0
    assert "No todos found" in result.output


def test_list_populated_todos(todo_invoke, add_todo):
    add_todo("some task")
    add_todo("second task")

    result = todo_invoke(["show"])

    assert result.exit_code == 0
    assert "1. some task" in result.output
    assert "2. second task" in result.output


def test_add_todo(todo_invoke):
    result = todo_invoke(["add", "some task"])

    assert result.exit_code == 0
    assert "1. some task" in result.output


def test_add_several_todo(todo_invoke):
    todo_invoke(["add", "some task"])

    result = todo_invoke(["add", "second task"])

    assert result.exit_code == 0
    assert "1. some task" in result.output
    assert "2. second task" in result.output


def test_remove_todo(todo_invoke, add_todo):
    add_todo("some task")
    add_todo("second task")

    result = todo_invoke(["remove", "1"])

    assert result.exit_code == 0
    assert "1. some task" not in result.output
    assert "1. second task" in result.output


def test_remove_all(todo_invoke, add_todo):
    add_todo("todo")
    add_todo("another tood")

    result = todo_invoke(["remove", "1", "2"])

    assert result.exit_code == 0

    show_result = todo_invoke(["show"])

    assert "No todos found" in show_result.output


def test_remove_todos(todo_invoke, add_todo):
    add_todo("todo 1")
    add_todo("todo 2")
    add_todo("todo 3")

    result = todo_invoke(["remove", "1", "3"])

    assert "deleted todos: [1, 3]" in result.output
    assert "1. todo 2" in result.output
