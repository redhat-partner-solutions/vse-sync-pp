### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.ppsdpll"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal

from vse_sync_pp.analyzers.ppsdpll import (
    TimeErrorAnalyzer
)

from .test_analyzer import AnalyzerTestBuilder

DPLLS = namedtuple('DPLLS', ('timestamp','eecstate', 'phasestate', 'phaseoffset',))

class TestTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.ppsdpll.TimeErrorAnalyzer"""
    constructor = TimeErrorAnalyzer
    id_ = 'ppsdpll/phase-offset-time-error'
    parser = 'dpll/phase-offset'
    expect = (
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 1,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(1)),
            ),
            'result': True,
            'reason': None,
            'analysis': {
                'duration': Decimal(2),
                'phaseoffset': {
                    'units': 'ns',
                    'min': 1,
                    'max': 1,
                    'range': 0,
                    'mean': 1,
                    'stddev': 0,
                    'variance': 0,
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
            ),
            'result': True,
            'reason': None,
            'analysis': {
                'duration': Decimal(2),
                'phaseoffset': {
                    'units': 'ns',
                    'min': 1,
                    'max': 1,
                    'range': 0,
                    'mean': 1,
                    'stddev': 0,
                    'variance': 0,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 4,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(1)),
                #oops lost sample
                DPLLS(Decimal('1876881.28'), 3, 3, Decimal(1)),
                DPLLS(Decimal('1876882.28'), 3, 3, Decimal(1)),
            ),
            'result': False,
            'reason': "short test samples",
            'analysis': {
                'duration': Decimal(4),
                'phaseoffset': {
                    'units': 'ns',
                    'min': 1,
                    'max': 1,
                    'range': 0,
                    'mean': 1,
                    'stddev': 0,
                    'variance': 0,
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
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(1)),
            ),
            'result': False,
            'reason': "short test duration",
            'analysis': {
                'duration': Decimal(2),
                'phaseoffset': {
                    'units': 'ns',
                    'min': 1,
                    'max': 1,
                    'range': 0,
                    'mean': 1,
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
                'min-test-duration/s': 1,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(-40)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(-39)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(-38)),
            ),
            'result': False,
            'reason': "unacceptable time error",
            'analysis': {
                'duration': Decimal(2),
                'phaseoffset': {
                    'units': 'ns',
                    'min': -40,
                    'max': -38,
                    'range': 2,
                    'mean': -39,
                    'stddev': 1,
                    'variance': 1,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 2,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(-40)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(-39)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(-38)),
            ),
            'result': False,
            'reason': "unacceptable time error",
            'analysis': {
                'duration': Decimal(2),
                'phaseoffset': {
                    'units': 'ns',
                    'min': -40,
                    'max': -38,
                    'range': 2,
                    'mean': -39,
                    'stddev': 1,
                    'variance': 1,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 3,
            },
            'rows': (
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(38)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(39)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(40)),
            ),
            'result': False,
            'reason': "short test duration",
            'analysis': {
                'duration': Decimal(2),
                'phaseoffset': {
                    'units': 'ns',
                    'min': 38,
                    'max': 40,
                    'range': 2,
                    'mean': 39,
                    'stddev': 1,
                    'variance': 1,
                },
            },
        },
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': {
                'time-error-limit/%': 100,
                'transient-period/s': 1,
                'min-test-duration/s': 3,
            },
            'rows': (
            ),
            'result': False,
            'reason': "no data",
            'analysis': {
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
                DPLLS(Decimal('1876878.28'), 3, 3, Decimal(38)),
                DPLLS(Decimal('1876879.28'), 3, 3, Decimal(39)),
                DPLLS(Decimal('1876880.28'), 3, 3, Decimal(40)),  
            ),
            'result': False,
            'reason': "unacceptable time error",
            'analysis': {
                'duration': Decimal(2),
                'phaseoffset': {
                    'units': 'ns',
                    'min': 38,
                    'max': 40,
                    'range': 2,
                    'mean': 39,
                    'stddev': 1,
                    'variance': 1,
                },
            },
        },
    )
