### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.ppsdpll"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal

from vse_sync_pp.analyzers.ppsdpll import (
    TimeErrorAnalyzer
)

from .test_analyzer import AnalyzerTestBuilder

DPO = namedtuple('DPO', ('phaseoffset',))

class TestTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.ppsdpll.TimeErrorAnalyzer"""
    constructor = TimeErrorAnalyzer
    id_ = 'ppsdpll/phase-offset-time-error'
    parser = 'dpll/phase-offset'
    expect = (
        {
            'requirements': 'G.8272/PRTC-A',
            'parameters': None,
            'rows': (
                DPO(Decimal(1)),
                DPO(Decimal(1)),
                DPO(Decimal(1)),
            ),
            'result': True,
            'reason': None,
            'analysis': {
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
            'parameters': None,
            'rows': (
                DPO(Decimal(1)),
                DPO(Decimal(1)),
                DPO(Decimal(1)),
            ),
            'result': True,
            'reason': None,
            'analysis': {
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
            'parameters': None,
            'rows': (
                DPO(Decimal(-40)),
                DPO(Decimal(-39)),
                DPO(Decimal(-38)),
            ),
            'result': True,
            'reason': None,
            'analysis': {
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
            'parameters': None,
            'rows': (
                DPO(Decimal(-40)),
                DPO(Decimal(-39)),
                DPO(Decimal(-38)),
            ),
            'result': False,
            'reason': None,
            'analysis': {
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
            'parameters': None,
            'rows': (
                DPO(Decimal(38)),
                DPO(Decimal(39)),
                DPO(Decimal(40)),
            ),
            'result': True,
            'reason': None,
            'analysis': {
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
            'requirements': 'G.8272/PRTC-B',
            'parameters': None,
            'rows': (
                DPO(Decimal(38)),
                DPO(Decimal(39)),
                DPO(Decimal(40)),
            ),
            'result': False,
            'reason': None,
            'analysis': {
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
