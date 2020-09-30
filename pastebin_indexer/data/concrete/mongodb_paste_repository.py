import os
from typing import List

from pymongo import MongoClient

from pastebin_indexer.data.contract.paste_repository import PasteRepository
from pastebin_indexer.domain.model import Paste


class MongoDBPasteRepository(PasteRepository):

    def __init__(self) -> None:
        host = os.environ.get("MONGODB_HOST", "localhost")
        username = os.environ.get("MONGODB_USER")
        password = os.environ.get("MONGODB_PWD")
        self.client = MongoClient("mongodb://{}:{}@{}:27017/".format(username,
                                                                     password,
                                                                     host))
        super().__init__()  # noqa

    def save(self, pastes: List[Paste]) -> None:

        with self.client.start_session():
            try:
                paste_collection = self.client["pastebindb"]["pastes"]
                documents = [paste.to_dict() for paste in pastes]
                paste_collection.insert_many(documents)
            except Exception as ex:
                self.logger.exception(ex)
