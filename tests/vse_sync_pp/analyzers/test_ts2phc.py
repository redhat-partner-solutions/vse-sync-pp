### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.ts2phc"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal
import math

from vse_sync_pp.analyzers.ts2phc import (
    TimeErrorAnalyzer
)

from .test_analyzer import AnalyzerTestBuilder

TERR = namedtuple('TERR', ('timestamp', 'terror', 'state'))

class TestTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.ts2phc.TimeErrorAnalyzer"""
    constructor = TimeErrorAnalyzer
    id_ = 'ts2phc/time-error'
    parser = 'ts2phc/time-error'
    expect = (
        # no data
        (
            'G.8272/PRTC-A',
            {
                'time-error-limit/%': 100,
                'transient-period/s': 6,
                'min-test-duration/s': 1,
            },
            (
                TERR(Decimal(0), 0, 's2'),
                TERR(Decimal(1), 0, 's2'),
                TERR(Decimal(2), 0, 's2'),
                TERR(Decimal(3), 0, 's2'),
                TERR(Decimal(4), 0, 's2'),
                TERR(Decimal(5), 0, 's2'),
            ),
            False,
            {},
        ),
        # loss of lock
        (
            'G.8272/PRTC-A',
            {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            (
                TERR(Decimal(0), 0, 's2'),
                # state s1 causes failure
                TERR(Decimal(1), 0, 's1'),
                TERR(Decimal(2), 0, 's2'),
                TERR(Decimal(3), 0, 's2'),
                TERR(Decimal(4), 0, 's2'),
                TERR(Decimal(5), 0, 's2'),
            ),
            False,
            {
                'duration': Decimal(4),
                'min': 0,
                'max': 0,
                'range': 0,
                'mean': 0,
                'stddev': 0,
                'variance': 0,
            },
        ),
        # unacceptable time error
        (
            'G.8272/PRTC-A',
            {
                'time-error-limit/%': 10,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            (
                TERR(Decimal(0),  0, 's2'),
                TERR(Decimal(1),  0, 's2'),
                TERR(Decimal(2),  0, 's2'),
                # terror of 10 is unacceptable
                TERR(Decimal(3), 10, 's2'),
                TERR(Decimal(4),  0, 's2'),
                TERR(Decimal(5),  0, 's2'),
            ),
            False,
            {
                'duration': Decimal(4),
                'min': 0,
                'max': 10,
                'range': 10,
                'mean': 2,
                'stddev': math.sqrt(20),
                'variance': 20,
            },
        ),
        # short test duration
        (
            'G.8272/PRTC-A',
            {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            (
                TERR(Decimal(0), 0, 's2'),
                TERR(Decimal(1), 0, 's2'),
                TERR(Decimal(2), 0, 's2'),
                TERR(Decimal(3), 0, 's2'),
                TERR(Decimal(4), 0, 's2'),
                # oops, window too short
            ),
            False,
            {
                'duration': Decimal(3),
                'min': 0,
                'max': 0,
                'range': 0,
                'mean': 0,
                'stddev': 0,
                'variance': 0,
            },
        ),
        # too few samples for test duration
        (
            'G.8272/PRTC-A',
            {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            (
                TERR(Decimal(0), 0, 's2'),
                TERR(Decimal(1), 0, 's2'),
                TERR(Decimal(2), 0, 's2'),
                TERR(Decimal(3), 0, 's2'),
                # oops, missing sample
                TERR(Decimal(5), 0, 's2'),
            ),
            False,
            {
                'duration': Decimal(4),
                'min': 0,
                'max': 0,
                'range': 0,
                'mean': 0,
                'stddev': 0,
                'variance': 0,
            },
        ),
        # success
        (
            'G.8272/PRTC-A',
            {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            (
                TERR(Decimal(0), 0, 's1'),
                TERR(Decimal(1), 0, 's2'),
                TERR(Decimal(2), 0, 's2'),
                TERR(Decimal(3), 0, 's2'),
                TERR(Decimal(4), 0, 's2'),
                TERR(Decimal(5), 0, 's2'),
            ),
            True,
            {
                'duration': Decimal(4),
                'min': 0,
                'max': 0,
                'range': 0,
                'mean': 0,
                'stddev': 0,
                'variance': 0,
            },
        ),
    )
