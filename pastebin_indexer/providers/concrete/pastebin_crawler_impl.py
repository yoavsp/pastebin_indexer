import concurrent.futures  # noqa
import os
from typing import List

import arrow
import lxml.html
import requests

from pastebin_indexer.config import ANONYMOUS_USER_NAMES, UNTITLED_TITLES
from pastebin_indexer.domain.model import Paste
from pastebin_indexer.providers.contract.pastebin_crawler \
    import PastebinCrawler
from pastebin_indexer.providers.exceptions import DOMChangedException


def sanitize_username(username: str) -> str:
    return username if username not in ANONYMOUS_USER_NAMES else ""


def sanitize_title(title) -> str:
    return title if title not in UNTITLED_TITLES else ""


class PastebinCrawlerImpl(PastebinCrawler):
    BASE_URL = "https://pastebin.com"

    def __init__(self) -> None:
        self.last_run_ids_cache = []

        super().__init__()  # noqa

    def get_pastes(self) -> List[Paste]:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [executor.submit(self.get_paste, paste_id.strip('/')) for
                       paste_id in self.get_paste_ids() if paste_id not in
                       self.last_run_ids_cache]

        pastes = [f.result() for f in concurrent.futures.as_completed(futures)]

        # This cache is a compromise between
        # code structure(not to expose concrete methods to the outside)
        # and performance(avoid visiting already stored items)
        self.last_run_ids_cache = [paste.id for paste in pastes]
        return pastes

    def get_paste_ids(self) -> List[str]:
        archive_html = requests.get(os.path.join(self.BASE_URL, "archive"))
        doc = lxml.html.fromstring(archive_html.content)
        link_elements = doc.xpath("//div[@class='archive-table']"
                                  "//td[span and a]/a[@href]")
        return [el.attrib.get('href') for el in link_elements
                if el.attrib.get('href')]

    def get_paste(self, paste_id: str) -> Paste:
        try:
            paste_html = requests.get(os.path.join(self.BASE_URL, paste_id))
            paste_doc = lxml.html.fromstring(paste_html.content)
            paste_title_element = paste_doc.xpath("//div[@class="
                                                  "'info-top']/h1")
            user_element = paste_doc.xpath("//div[@class='username']/a")
            date_element = paste_doc.xpath("//div[@class='date']"
                                           "/span[@title and "
                                           "text()!='edited']/@title")
            content_element = paste_doc.find_class("textarea")
            if([] in [paste_title_element,
                      user_element,
                      date_element,
                      content_element]):
                raise DOMChangedException()

            paste_title = paste_title_element[0].text
            username = user_element[0].text

            paste_date = arrow.get(date_element[0]
                                   .replace("CDT", "US/Central"),
                                   "dddd DD[th] [of] MMMM YYYY HH:mm:ss A ZZZ")

            content = content_element[0].value.strip("\r\n ")
            paste = Paste(paste_id,
                          sanitize_username(username),
                          sanitize_title(paste_title),
                          paste_date,
                          content)
            return paste

        except Exception as e:
            self.logger.exception(e)
            raise
