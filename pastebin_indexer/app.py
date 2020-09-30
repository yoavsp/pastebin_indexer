import sched
import time
from logging import getLogger

from pastebin_indexer.config import get_paste_repository
from pastebin_indexer.domain.pastebin_controller \
    import PastebinController
from pastebin_indexer.providers.concrete.pastebin_crawler_impl \
    import PastebinCrawlerImpl

logger = getLogger(__name__)


def crawl_pastebin(sc: sched.scheduler, pbc: PastebinController):
    logger.info("crawl_pastebin: started...")
    pbc.run()
    sc.enter(20, 1, crawl_pastebin, (sc, pbc,))
    logger.info("crawl_pastebin: done")


if __name__ == "__main__":
    coordinator = PastebinController(get_paste_repository(),
                                     PastebinCrawlerImpl())
    scheduler = sched.scheduler(time.time, time.sleep)

    scheduler.enter(0, 1, crawl_pastebin, (scheduler, coordinator,))
    scheduler.run()
