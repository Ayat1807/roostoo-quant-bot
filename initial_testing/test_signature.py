"""Offline unit tests: signing, number formatting and the testing-key guard.

Runs with no network and no keys:  python test_signature.py
"""

from __future__ import annotations

import unittest
from decimal import Decimal

from roostoo_client import (
    KeySafetyError,
    RoostooClient,
    fmt_decimal,
    mask_key,
    round_to_precision,
    sign,
)

# Public example values from the official Roostoo API documentation.
DOC_SECRET = "S1XP1e3UZj6A7H5fATj0jNhqPxxdSJYdInClVN65XAbvqqMKjVHjA7PZj4W12oep"
DOC_PARAMS = {
    "pair": "BNB/USD",
    "quantity": "2000",
    "side": "BUY",
    "timestamp": "1580774512000",
    "type": "MARKET",
}
DOC_TOTAL_PARAMS = "pair=BNB/USD&quantity=2000&side=BUY&timestamp=1580774512000&type=MARKET"
DOC_SIGNATURE = "20b7fd5550b67b3bf0c1684ed0f04885261db8fdabd38611e9e6af23c19b7fff"


class TestSignature(unittest.TestCase):
    def test_docs_example(self) -> None:
        total, sig = sign(DOC_SECRET, DOC_PARAMS)
        self.assertEqual(total, DOC_TOTAL_PARAMS)
        self.assertEqual(sig, DOC_SIGNATURE)

    def test_param_order_does_not_matter(self) -> None:
        shuffled = dict(reversed(list(DOC_PARAMS.items())))
        self.assertEqual(sign(DOC_SECRET, shuffled)[1], DOC_SIGNATURE)


class TestHelpers(unittest.TestCase):
    def test_fmt_decimal_never_scientific(self) -> None:
        self.assertEqual(fmt_decimal(0.00001), "0.00001")
        self.assertEqual(fmt_decimal(2000.0), "2000")
        self.assertEqual(fmt_decimal(Decimal("1.2300")), "1.23")

    def test_quantity_rounds_down(self) -> None:
        self.assertEqual(round_to_precision(0.123456789, 5), Decimal("0.12345"))
        self.assertEqual(round_to_precision(0.123451, 5, down=False), Decimal("0.12346"))

    def test_mask_key(self) -> None:
        self.assertEqual(mask_key("ABCDEFGHIJ"), "ABCD****")


class TestKeyGuard(unittest.TestCase):
    def test_competition_label_refused(self) -> None:
        c = RoostooClient("k" * 10, "s" * 10, key_label="competition")
        with self.assertRaises(KeySafetyError):
            c.balance()  # must fail before any network call

    def test_secret_not_in_repr(self) -> None:
        c = RoostooClient("ABCDEFGHIJ", "SUPERSECRET", key_label="testing")
        self.assertNotIn("SUPERSECRET", repr(c))
        self.assertNotIn("EFGHIJ", repr(c))


if __name__ == "__main__":
    unittest.main(verbosity=2)
