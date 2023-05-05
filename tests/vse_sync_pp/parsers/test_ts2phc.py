### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.parsers.ts2phc"""

from unittest import TestCase
from decimal import Decimal

from vse_sync_pp.parsers.ts2phc import (
    TimeError,
)

from .test_parser import ParserTestBuilder

class TestTimeError(TestCase, metaclass=ParserTestBuilder):
    """Test cases for vse_sync_pp.parsers.ts2phc.TimeError"""
    constructor = TimeError
    id_ = 'ts2phc/time-error'
    elems = ('timestamp', 'interface', 'terror', 'state')
    accept = (
        (   'ts2phc[681011.839]: [ts2phc.0.config] '
            'ens7f1 master offset          0 s2 freq      -0',
            (Decimal('681011.839'), 'ens7f1', 0, 's2'),
        ),
    )
    reject = (
        'foo bar baz',
    )
