### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.gnss"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal
import math

from vse_sync_pp.analyzers.gnss import (
    TimeErrorAnalyzer
)

from .test_analyzer import AnalyzerTestBuilder

TERR = namedtuple('TERR', ('timestamp', 'terror', 'state'))

class TestTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.gnss.TimeErrorAnalyzer"""
    constructor = TimeErrorAnalyzer
    id_ = 'gnss/time-error'
    parser = 'gnss/time-error'
    expect = (
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 1,
            },
            'rows': (),
            'result': False,
            'reason': "no data",
            'analysis': {},
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 6,
                'min-test-duration/s': 1,
            },
            'rows': (
                TERR(Decimal(0), 0, 5),
                TERR(Decimal(1), 0, 5),
                TERR(Decimal(2), 0, 5),
                TERR(Decimal(3), 0, 5),
                TERR(Decimal(4), 0, 5),
                TERR(Decimal(5), 0, 5),
            ),
            'result': False,
            'reason': "no data",
            'analysis': {},
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 5),
                # state 1 causes failure
                TERR(Decimal(1), 0, 1),
                TERR(Decimal(2), 0, 5),
                TERR(Decimal(3), 0, 5),
                TERR(Decimal(4), 0, 5),
                TERR(Decimal(5), 0, 5),
            ),
            'result': False,
            'reason': "loss of lock",
            'analysis': {
                'duration': Decimal(4),
                'terror': {
                    'units': 'ns',
                    'min': 0,
                    'max': 0,
                    'range': 0,
                    'mean': 0,
                    'stddev': 0,
                    'variance': 0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 10,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0),  0, 5),
                TERR(Decimal(1),  0, 5),
                TERR(Decimal(2),  0, 5),
                # terror of 10 is unacceptable
                TERR(Decimal(3), 10, 5),
                TERR(Decimal(4),  0, 5),
                TERR(Decimal(5),  0, 5),
            ),
            'result': False,
            'reason': "unacceptable time error",
            'analysis': {
                'duration': Decimal(4),
                'terror': {
                    'units': 'ns',
                    'min': 0,
                    'max': 10,
                    'range': 10,
                    'mean': 2,
                    'stddev': round(math.sqrt(20), 3),
                    'variance': 20.0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 5),
                TERR(Decimal(1), 0, 5),
                TERR(Decimal(2), 0, 5),
                TERR(Decimal(3), 0, 5),
                TERR(Decimal(4), 0, 5),
                # oops, window too short
            ),
            'result': False,
            'reason': "short test duration",
            'analysis': {
                'duration': Decimal(3),
                'terror': {
                    'units': 'ns',
                    'min': 0,
                    'max': 0,
                    'range': 0,
                    'mean': 0,
                    'stddev': 0,
                    'variance': 0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 5),
                TERR(Decimal(1), 0, 5),
                TERR(Decimal(2), 0, 5),
                TERR(Decimal(3), 0, 5),
                # oops, missing sample
                TERR(Decimal(5), 0, 5),
            ),
            'result': False,
            'reason': "short test samples",
            'analysis': {
                'duration': Decimal(4),
                'terror': {
                    'units': 'ns',
                    'min': 0,
                    'max': 0,
                    'range': 0,
                    'mean': 0,
                    'stddev': 0,
                    'variance': 0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 1),
                TERR(Decimal(1), 0, 5),
                TERR(Decimal(2), 0, 5),
                TERR(Decimal(3), 0, 5),
                TERR(Decimal(4), 0, 5),
                TERR(Decimal(5), 0, 5),
            ),
            'result': True,
            'reason': None,
            'analysis': {
                'duration': Decimal(4),
                'terror': {
                    'units': 'ns',
                    'min': 0,
                    'max': 0,
                    'range': 0,
                    'mean': 0,
                    'stddev': 0,
                    'variance': 0,
                },
            },
        },
    )
