### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ts2phc log messages"""

from .analyzer import TimeErrorAnalyzerBase

class TimeErrorAnalyzer(TimeErrorAnalyzerBase):
    """Analyze time error"""
    id_ = 'ts2phc/time-error'
    parser = id_
    lockid = frozenset({'s2'})
