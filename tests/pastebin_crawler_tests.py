from unittest import TestCase, mock
from unittest.mock import MagicMock, patch

from lxml import etree

import pastebin_indexer
from pastebin_indexer.providers.concrete.pastebin_crawler_impl \
    import PastebinCrawlerImpl
from pastebin_indexer.providers.exceptions import DOMChangedException


class PastebinCrawlerImplTests(TestCase):

    def test_xml_source_changed(self):
        with mock.patch('requests.get', autospec=True) as mock_get:
            mock_get.return_value.content = b"<html/>"

            crawler = PastebinCrawlerImpl()
            with self.assertRaises(DOMChangedException) as context:
                crawler.get_paste("some_id")

