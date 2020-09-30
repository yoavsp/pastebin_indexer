from abc import ABC, abstractmethod
from logging import getLogger
from typing import List

from pastebin_indexer.domain.model import Paste


class PastebinCrawler(ABC):

    def __init__(self) -> None:
        self.logger = getLogger(__name__)
        super().__init__()  # noqa

    @abstractmethod
    def get_pastes(self) -> List[Paste]:
        pass
