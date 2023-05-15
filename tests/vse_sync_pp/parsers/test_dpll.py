### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.parsers.dpll"""

from unittest import TestCase
from decimal import Decimal

from vse_sync_pp.parsers.dpll import (
    PhaseOffset,
)

from .test_parser import ParserTestBuilder

class TestPhaseOffset(TestCase, metaclass=ParserTestBuilder):
    """Test cases for vse_sync_pp.parsers.dpll.PhaseOffset"""
    constructor = PhaseOffset
    id_ = 'dpll/phase-offset'
    elems = ('timestamp', 'eecstate', 'phasestate', 'phaseoffset')
    accept = (
        (   '1876878.28,3,3,-0.79',
            (Decimal('1876878.28'), 3, 3, Decimal('-0.79')),
        ),
    )
    reject = (
        'foo bar baz',
        '3,3,-0.79',
        '1876878.28,3,3,-0.79,9',
        'quux,3,3,-0.79',
        '1876878.28,quux,3,-0.79',
        '1876878.28,3,quux,-0.79',
        '1876878.28,3,3,quux',
    )
    discard = ()
