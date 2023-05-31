### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.ppsdpll"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal

from vse_sync_pp.analyzers.ppsdpll import (
    PhaseOffsetTimeErrorAnalyzer
)

from .test_analyzer import AnalyzerTestBuilder

DPO = namedtuple('DPO', ('phaseoffset',))

class TestPhaseOffsetTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.ppsdpll.PhaseOffsetTimeErrorAnalyzer"""
    constructor = PhaseOffsetTimeErrorAnalyzer
    id_ = 'ppsdpll/phase-offset-time-error'
    parser = 'dpll/phase-offset'
    expect = (
        (
            'G.8272/PRTC-A',
            None,
            (
                DPO(Decimal(1)),
                DPO(Decimal(1)),
                DPO(Decimal(1)),
            ),
            True,
            None,
            {
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
        ),
        (
            'G.8272/PRTC-B',
            None,
            (
                DPO(Decimal(1)),
                DPO(Decimal(1)),
                DPO(Decimal(1)),
            ),
            True,
            None,
            {
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
        ),
        (
            'G.8272/PRTC-A',
            None,
            (
                DPO(Decimal(-40)),
                DPO(Decimal(-39)),
                DPO(Decimal(-38)),
            ),
            True,
            None,
            {
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
        ),
        (
            'G.8272/PRTC-B',
            None,
            (
                DPO(Decimal(-40)),
                DPO(Decimal(-39)),
                DPO(Decimal(-38)),
            ),
            False,
            None,
            {
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
        ),
        (
            'G.8272/PRTC-A',
            None,
            (
                DPO(Decimal(38)),
                DPO(Decimal(39)),
                DPO(Decimal(40)),
            ),
            True,
            None,
            {
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
        ),
        (
            'G.8272/PRTC-B',
            None,
            (
                DPO(Decimal(38)),
                DPO(Decimal(39)),
                DPO(Decimal(40)),
            ),
            False,
            None,
            {
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
        ),
    )
