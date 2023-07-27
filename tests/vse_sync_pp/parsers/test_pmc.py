### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.parsers.pmc"""

from unittest import TestCase
from decimal import Decimal

from vse_sync_pp.parsers.pmc import (
    ClockClassParser,
)

from .test_parser import ParserTestBuilder

class TestClockClassParser(TestCase, metaclass=ParserTestBuilder):
    """Test cases for vse_sync_pp.parsers.pmc.TestClockClassParser"""
    constructor = ClockClassParser
    id_ = 'phc/gm-settings'
    elems = ('timestamp', 'clock_class')
    accept = (
        #FreeRun class id: 248
        (   '681011.839,248,foo',
            (Decimal('681011.839'), 248),
        ),
        #Locked class id: 6
        (
            '2023-06-16T17:01:11.131Z,6,foo',
            (Decimal('1686934871.131'), 6),
        ),
        #Holdover class ids: 7,140,150,160
        (
            '2023-06-16T17:01:11.131282-00:00,7,foo',
            (Decimal('1686934871.131282'), 7),
        ),
        (
            '2023-06-16T17:01:11.131282269+00:00,140,foo',
            (Decimal('1686934871.131282269'), 140),
        ),
        (   '681011.839,150,foo',
            (Decimal('681011.839'), 150),
        ),
        (   '681011.839,160,foo',
            (Decimal('681011.839'), 160),
        ),
    )
    reject = (
        'foo bar baz',
        'quux,3,3',
        '1876878.28,quux,3',
        '2023-06-16T17:01Z,5,-3',
        '2023-06-16T17:01:00Z,5,-3',
        '2023-06-16T17:01:00.123+01:00,5,-3',
        '2023-06-16T17:01:00,123+00:00,5,-3',
    )
    discard = ()
    file = (
        '\n'.join((
            '847914.839,248',
            '847915.839,6',
            '847916.839,7',

        )),
        (
            (Decimal('847914.839'), 248),
            (Decimal('847915.839'), 6),
            (Decimal('847916.839'), 7),
        ),
    )
