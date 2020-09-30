from unittest import TestCase
import arrow

from pastebin_indexer.domain.model import Paste


class ModelTests(TestCase):

    def test_paste_date_serialization(self):
        paste = Paste("an_id", "user #1", "best paste ever", arrow.utcnow(), "best content ever")
        paste_dict = paste.to_dict()
        self.assertEqual(type(paste_dict['date']), float)
        self.assertEqual(Paste.from_dict(paste.to_dict()), paste)
        self.assertEqual(Paste.from_json(paste.to_json()), paste)
