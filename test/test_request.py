# system library
import unittest
from datetime import datetime

# project library
from cstock.hexun_engine import HexunEngine
from cstock.sina_engine import SinaEngine
from cstock.request import Requester
from cstock.model import Stock

class TestRequester(unittest.TestCase):

    def setUp(self):
        engine = HexunEngine()
        self.hexun_requester = Requester(engine)
        engine = SinaEngine()
        self.sina_requester = Requester(engine)

    def test_request(self):
        stock = self.hexun_requester.request('000626')
        self.assertEqual(stock.__class__, Stock)

        stock = self.sina_requester.request('002475')
        self.assertEqual(stock.__class__, Stock)