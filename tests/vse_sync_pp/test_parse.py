### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.parsers"""

import json
from decimal import Decimal

from unittest import TestCase

from vse_sync_pp.parse import (
    DecimalEncoder,
)

class TestDecimalEncoder(TestCase):
    """Test cases for vse_sync_pp.parse.DecimalEncoder"""
    def test_encode(self):
        """Test vse_sync_pp.parse.DecimalEncoder encodes Decimal"""
        self.assertEqual(
            json.dumps(Decimal('123.456'), cls=DecimalEncoder),
            '123.456',
        )
