from typing import List

import antodo


class TodosLoader:
    def __init__(self, storage=None):
        if storage is None:
            storage = antodo.TodosJSONStorage(path=antodo.config.TODOS_JSON_PATH)
        self.storage = storage

    def load_todos(self) -> List[antodo.Todo]:
        return self.storage.get_todos()

    def save_todos(self, todos: antodo.Todos):
        self.storage.save_todos(todos)

    def load_archive(self) -> List[antodo.Todo]:
        return self.storage.get_archive()

    def save_archive(self, archive: List[str]):
        self.storage.save_archive(archive)
