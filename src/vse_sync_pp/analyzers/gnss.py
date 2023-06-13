### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze GNSS log messages"""

from .analyzer import TimeErrorAnalyzerBase

class TimeErrorAnalyzer(TimeErrorAnalyzerBase):
    """Analyze time error"""
    id_ = 'gnss/time-error'
    parser = id_
    # 'state' values are assumed to be u-blox gpsFix values
    # 0 = no fix
    # 1 = dead reckoning only
    # 2 = 2D-Fix
    # 3 = 3D-Fix
    # 4 = GPS + dead reckoning combined
    # 5 = time only fix
    locked = frozenset({3, 4, 5})
