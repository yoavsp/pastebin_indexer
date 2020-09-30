from abc import ABC, abstractmethod
from logging import getLogger
from typing import List

from pastebin_indexer.domain.model import Paste


class PasteRepository(ABC):
    def __init__(self) -> None:
        self.logger = getLogger(__name__)
        super().__init__() # noqa

    @abstractmethod
    def save(self, pastes: List[Paste]) -> None:
        pass
