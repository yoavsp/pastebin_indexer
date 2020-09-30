import os
from typing import List

from tinydb import TinyDB

from pastebin_indexer.data.contract.paste_repository import PasteRepository
from pastebin_indexer.domain.model import Paste


class TinyDBPasteRepository(PasteRepository):
    TABLE_NAME = "pastes"

    def __init__(self) -> None:
        super().__init__()  # noqa
        path = os.environ.get("TINYDB_FILE_PATH")
        assert path and os.path.exists(path)
        self.path = path

    def save(self, pastes: List[Paste]) -> None:
        with TinyDB(self.path) as db:
            db.table(self.TABLE_NAME).insert_multiple([paste.to_dict()
                                                       for paste in pastes])
