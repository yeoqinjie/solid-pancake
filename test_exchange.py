from unittest import TestCase
from exchange import CurrencyExchange


class TestCurrencyExchange(TestCase):
    def test_exchange_sgd_usd(self):
        self.assertEqual(CurrencyExchange.exchange_sgd_usd(1), 0.7)

    def test_exchange_usd_sgd(self):
        self.assertEqual(CurrencyExchange.exchange_usd_sgd(1), 1.4)

    def test_exchange_sgd_usd2(self):
        self.assertEqual(CurrencyExchange.exchange_sgd_usd(10), 7)

    def test_exchange_sgd_usd3(self):
        self.assertEqual(CurrencyExchange.exchange_sgd_usd(11), 8.7)
