### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.parsers.gnss"""

from unittest import TestCase
from decimal import Decimal

from vse_sync_pp.parsers.gnss import (
    TimeErrorParser,
)

from .test_parser import ParserTestBuilder

class TestTimeErrorParser(TestCase, metaclass=ParserTestBuilder):
    """Test cases for vse_sync_pp.parsers.gnss.TimeErrorParser"""
    constructor = TimeErrorParser
    id_ = 'gnss/time-error'
    elems = ('timestamp', 'state', 'terror')
    accept = (
        (   '681011.839,5,-3',
            (Decimal('681011.839'), 5, -3),
        ),
    )
    reject = (
        'foo bar baz',
        '1876878.28,3',
        'quux,3,3',
        '1876878.28,quux,3',
        '1876878.28,3,quux',
    )
    discard = ()
    file = (
        '\n'.join((
            '847914.839,3,4',
            '847915.839,5,-1',
        )),
        (
            (Decimal('847914.839'), 3, 4),
            (Decimal('847915.839'), 5, -1),
        ),
    )
