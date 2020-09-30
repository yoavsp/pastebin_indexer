import os

from pastebin_indexer.data.concrete.mongodb_paste_repository \
    import MongoDBPasteRepository
from pastebin_indexer.data.concrete.tinydb_paste_repository \
    import TinyDBPasteRepository
from pastebin_indexer.data.contract.paste_repository import PasteRepository

ANONYMOUS_USER_NAMES = os.environ.get("ANONYMOUS_USER_NAMES", [])

UNTITLED_TITLES = os.environ.get("UNTITLED_TITLES", [])


def get_paste_repository() -> PasteRepository:
    return MongoDBPasteRepository() if \
        os.environ.get("PASTE_REPO_TYPE") == "MONGO" \
        else TinyDBPasteRepository()
