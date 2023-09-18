### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.phc2sys"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal
import math

from vse_sync_pp.analyzers.phc2sys import TimeErrorAnalyzer

from .test_analyzer import AnalyzerTestBuilder

TERR = namedtuple('TERR', ('timestamp', 'terror', 'state', 'delay'))

class TestTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.phc2sys.TimeErrorAnalyzer"""
    constructor = TimeErrorAnalyzer
    id_ = 'phc2sys/time-error'
    parser = 'phc2sys/time-error'
    expect = (
        {
            'requirements': 'workload/RAN',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 1,
            },
            'rows': (),
            'result': False,
            'reason': "no data",
            'timestamp': None,
            'duration': None,
            'analysis': {},
        },
        {
            'requirements': 'workload/RAN',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 6,
                'min-test-duration/s': 1,
            },
            'rows': (
                TERR(Decimal(0), 0, 's2', 620),
                TERR(Decimal(1), 0, 's2', 620),
                TERR(Decimal(2), 0, 's2', 620),
                TERR(Decimal(3), 0, 's2', 620),
                TERR(Decimal(4), 0, 's2', 620),
                TERR(Decimal(5), 0, 's2', 620),
            ),
            'result': False,
            'reason': "no data",
            'timestamp': None,
            'duration': None,
            'analysis': {},
        },
        {
            'requirements': 'workload/RAN',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 's2', 620),
                # state s1 causes failure
                TERR(Decimal(1), 0, 's1', 620),
                TERR(Decimal(2), 0, 's2', 620),
                TERR(Decimal(3), 0, 's2', 620),
                TERR(Decimal(4), 0, 's2', 620),
                TERR(Decimal(5), 0, 's2', 620),
            ),
            'result': False,
            'reason': "loss of lock",
            'timestamp': Decimal(1),
            'duration': Decimal(4),
            'analysis': {
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
            'requirements': 'workload/RAN',
            'parameters': {
                'time-error-limit/%': 10,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0),  0, 's2', 620),
                TERR(Decimal(1),  0, 's2', 620),
                TERR(Decimal(2),  0, 's2', 620),
                # terror of 10 is unacceptable
                TERR(Decimal(3), 10, 's2', 620),
                TERR(Decimal(4),  0, 's2', 620),
                TERR(Decimal(5),  0, 's2', 620),
            ),
            'result': False,
            'reason': "unacceptable time error",
            'timestamp': Decimal(1),
            'duration': Decimal(4),
            'analysis': {
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
            'requirements': 'workload/RAN',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 's2', 620),
                TERR(Decimal(1), 0, 's2', 620),
                TERR(Decimal(2), 0, 's2', 620),
                TERR(Decimal(3), 0, 's2', 620),
                TERR(Decimal(4), 0, 's2', 620),
                # oops, window too short
            ),
            'result': False,
            'reason': "short test duration",
            'timestamp': Decimal(1),
            'duration': Decimal(3),
            'analysis': {
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
            'requirements': 'workload/RAN',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 's2', 620),
                TERR(Decimal(1), 0, 's2', 620),
                TERR(Decimal(2), 0, 's2', 620),
                TERR(Decimal(3), 0, 's2', 620),
                # oops, missing sample
                TERR(Decimal(5), 0, 's2', 620),
            ),
            'result': False,
            'reason': "short test samples",
            'timestamp': Decimal(1),
            'duration': Decimal(4),
            'analysis': {
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
            'requirements': 'workload/RAN',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                TERR(Decimal(0), 0, 's1', 620),
                TERR(Decimal(1), 0, 's2', 620),
                TERR(Decimal(2), 0, 's2', 620),
                TERR(Decimal(3), 0, 's2', 620),
                TERR(Decimal(4), 0, 's2', 620),
                TERR(Decimal(5), 0, 's2', 620),
            ),
            'result': True,
            'reason': None,
            'timestamp': Decimal(1),
            'duration': Decimal(4),
            'analysis': {
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
