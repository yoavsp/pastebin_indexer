from logging import getLogger

from pastebin_indexer.data.contract.paste_repository import PasteRepository
from pastebin_indexer.providers.contract.pastebin_crawler \
    import PastebinCrawler


class PastebinController:
    def __init__(self, repository: PasteRepository,
                 crawler: PastebinCrawler) -> None:
        self.repository = repository
        self.crawler = crawler
        self.logger = getLogger(__name__)
        self.logger.info("started")
        self.logger.debug("running with "
                          "{} and {}".format(repository.__class__.__name__,
                                             crawler.__class__.__name__))

    def run(self):
        self.logger.info("job start: crawling")
        pastes = self.crawler.get_pastes()
        self.logger.info("inserting pastes to datastore")
        self.repository.save(pastes)
