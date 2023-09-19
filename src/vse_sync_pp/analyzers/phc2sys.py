### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze phc2sys log messages"""

from .analyzer import TimeErrorAnalyzerBase


class TimeErrorAnalyzer(TimeErrorAnalyzerBase):
    """Analyze time error"""
    id_ = 'phc2sys/time-error'
    parser = id_
    locked = frozenset({'s2'})
