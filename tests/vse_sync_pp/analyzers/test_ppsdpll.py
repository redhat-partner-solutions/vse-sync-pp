### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.ppsdpll"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal

from vse_sync_pp.analyzers.ppsdpll import (
    PhaseOffsetTimeErrorAnalyzer,
    PhaseOffsetConstantTimeErrorAnalyzer
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
            (
                DPO(Decimal(1)),
                DPO(Decimal(1)),
                DPO(Decimal(1)),
            ),
            True,
            {
                'units': 'ns',
                'min': 1,
                'max': 1,
                'range': 0,
                'mean': 1,
                'stddev': 0,
                'variance': 0,
            },
        ),
        (
            (
                DPO(Decimal(-40)),
                DPO(Decimal(-39)),
                DPO(Decimal(-38)),
            ),
            False,
            {
                'units': 'ns',
                'min': -40,
                'max': -38,
                'range': 2,
                'mean': -39,
                'stddev': 1,
                'variance': 1,
            },
        ),
        (
            (
                DPO(Decimal(38)),
                DPO(Decimal(39)),
                DPO(Decimal(40)),
            ),
            False,
            {
                'units': 'ns',
                'min': 38,
                'max': 40,
                'range': 2,
                'mean': 39,
                'stddev': 1,
                'variance': 1,
            },
        ),
    )

class TestPhaseOffsetConstantTimeErrorAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.ppsdpll.PhaseOffsetConstantTimeErrorAnalyzer"""
    constructor = PhaseOffsetConstantTimeErrorAnalyzer
    id_ = 'ppsdpll/phase-offset-constant-time-error'
    parser = 'dpll/phase-offset'
    expect = (
        (
            (
                DPO(Decimal(1)),
                DPO(Decimal(1)),
                DPO(Decimal(1)),
            ),
            True,
            {
                'units': 'ns',
                'min': 1,
                'max': 1,
                'range': 0,
                'mean': 1,
                'stddev': 0,
                'variance': 0,
            },
        ),
        (
            (
                DPO(Decimal(-40)),
                DPO(Decimal(-39)),
                DPO(Decimal(-38)),
            ),
            False,
            {
                'units': 'ns',
                'min': -40,
                'max': -38,
                'range': 2,
                'mean': -39,
                'stddev': 1,
                'variance': 1,
            },
        ),
        (
            (
                DPO(Decimal(38)),
                DPO(Decimal(39)),
                DPO(Decimal(40)),
            ),
            False,
            {
                'units': 'ns',
                'min': 38,
                'max': 40,
                'range': 2,
                'mean': 39,
                'stddev': 1,
                'variance': 1,
            },
        ),
    )
