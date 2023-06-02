### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.ppsdpll"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal

from vse_sync_pp.analyzers.ppsdpll import (
    TimeErrorAnalyzer
)

from .test_analyzer import AnalyzerTestBuilder

DPLLS = namedtuple('DPLLS', ('timestamp','eecstate', 'state', 'terror',))

class TestTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.ppsdpll.TimeErrorAnalyzer"""
    constructor = TimeErrorAnalyzer
    id_ = 'ppsdpll/time-error'
    parser = 'dpll/time-error'
    expect = (
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 3,
            },
            'rows': (),
            'result': False,
            'reason': "no data",
            'analysis': {},
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 3,
                'min-test-duration/s': 1,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(1)),
            ),
            'result': False,
            'reason': "no data",
            'analysis': {},
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 1,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(1)),
                # state 2 causes failure
                DPLLS(Decimal('1876879.28'), 3, 2, Decimal(1)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(1)),
            ),
            'result': False,
            'reason': "loss of lock",
            'analysis': {
                'duration': Decimal(1.0),
                'terror': {
                    'units': 'ns',
                    'min': 1.0,
                    'max': 1.0,
                    'range': 0.0,
                    'mean': 1.0,
                    'stddev': 0.0,
                    'variance': 0.0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 10,
                'transient-period/s': 1,
                'min-test-duration/s': 1,
            },
            'rows': (
                DPLLS(Decimal('1876877.28'), 3, 3, Decimal(-40)),
                # terror of -40 is unacceptable
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(-40)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(-39)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(-38)),
            ),
            'result': False,
            'reason': "unacceptable time error",
            'analysis': {
                'duration': Decimal(2.0),
                'terror': {
                    'units': 'ns',
                    'min': -40.0,
                    'max': -38.0,
                    'range': 2.0,
                    'mean': -39.0,
                    'stddev': 1.0,
                    'variance': 1.0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 3,
            },
            'rows': (
                DPLLS(Decimal('1876877.28'), 3, 3, Decimal(37)),
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(37)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(38)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(39)),
                # oops, window too short
            ),
            'result': False,
            'reason': "short test duration",
            'analysis': {
                'duration': Decimal(2.0),
                'terror': {
                    'units': 'ns',
                    'min': 37.0,
                    'max': 39.0,
                    'range': 2.0,
                    'mean': 38.0,
                    'stddev': 1.0,
                    'variance': 1.0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 3,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(1)),
                # oops, lost sample
                DPLLS(Decimal('1876881.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876882.28'), 3, 3, Decimal(1)),
            ),
            'result': False,
            'reason': "short test samples",
            'analysis': {
                'duration': Decimal(3.0),
                'terror': {
                    'units': 'ns',
                    'min': 1.0,
                    'max': 1.0,
                    'range': 0.0,
                    'mean': 1.0,
                    'stddev': 0.0,
                    'variance': 0.0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 1,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876881.28'), 3, 3, Decimal(1)),
            ),
            'result': True,
            'reason': None,
            'analysis': {
                'duration': Decimal(2.0),
                'terror': {
                    'units': 'ns',
                    'min': 1.0,
                    'max': 1.0,
                    'range': 0.0,
                    'mean': 1.0,
                    'stddev': 0.0,
                    'variance': 0.0,
                },
            },
        },
    )
