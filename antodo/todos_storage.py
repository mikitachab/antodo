import os
import json
from typing import List

import safer

import antodo


class TodosJSONStorage:
    DEFAULT_STORAGE: dict = {"todos": [], "archive": []}

    def __init__(self, path):
        self.path = path
        self.dir = os.path.dirname(path)

    def get_todos(self) -> List[antodo.Todo]:
        storage = self.get_or_create_storage()
        todos = storage["todos"]
        return list(map(lambda todo: antodo.Todo(**todo), todos))

    def get_archive(self) -> List[str]:
        storage = self.get_or_create_storage()
        return storage["archive"]

    def get_or_create_storage(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path) as file:
                return json.load(file)

        os.makedirs(self.dir, exist_ok=True)
        with safer.open(self.path, "w") as file:
            json.dump(self.DEFAULT_STORAGE, file)

        return self.DEFAULT_STORAGE

    def save(self, storage: dict):
        with safer.open(self.path, "w") as file:
            json.dump(storage, file)

    def save_todos(self, todos: antodo.Todos):
        storage = self.get_or_create_storage()
        storage["todos"] = todos.to_json()
        self.save(storage)

    def save_archive(self, archive: List[str]):
        storage = self.get_or_create_storage()
        storage["archive"] = archive
        self.save(storage)
