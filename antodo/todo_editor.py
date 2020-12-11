import os
import tempfile

import antodo


class TodoEditorError(Exception):
    pass


class TodoEditor:
    def __init__(self, todo):
        self._todo: antodo.Todo = todo
        self._editor = os.getenv("EDITOR")
        if self._editor is None:
            raise TodoEditorError("env var EDITOR not set")

    def get_new_todo_content(self):
        path = _get_tempfile_with_content(self._todo.content)
        self._run_file_editing(path)
        new_content = _read_file(path)
        return _clean_content(new_content)

    def get_new_todo_subtask_content(self, index: int):
        path = _get_tempfile_with_content(self._todo.subtasks[index])
        self._run_file_editing(path)
        new_content = _read_file(path)
        return _clean_content(new_content)

    def _run_file_editing(self, path):
        try:
            os.system(f"{self._editor} {path}")
        except Exception as error:
            raise TodoEditorError(error)


def _clean_content(content):
    return content.replace("\n", "")


def _read_file(path):
    with open(path) as file:
        return file.read()


def _get_tempfile_with_content(content: str):
    path = _get_templfile()
    with open(path, "w") as file:
        file.write(content)
    return path


def _get_templfile():
    file, path = tempfile.mkstemp()
    os.close(file)
    return path
