### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze GNSS log messages"""

from .analyzer import TimeErrorAnalyzerBase

class TimeErrorAnalyzer(TimeErrorAnalyzerBase):
    """Analyze time error"""
    id_ = 'gnss/time-error'
    parser = id_
    locked = frozenset({3, 4, 5})
