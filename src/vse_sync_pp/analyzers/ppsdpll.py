### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ppsdpll log messages"""

from .analyzer import TimeErrorAnalyzerBase

class TimeErrorAnalyzer(TimeErrorAnalyzerBase):
    """Analyze DPLL time error"""
    id_ = 'ppsdpll/time-error'
    parser = 'dpll/time-error'
    # 'state' unlocked
    # -1 = DPLL_UNKNOWN
    #  0 = DPLL_INVALID
    #  1 = DPLL_FREERUN
    # 'state' locked and operational
    # 2 = DPLL_LOCKED
    # 3 = DPLL_LOCKED HOLDOVER ACQUIRED
    # 'state' unlocked but operational
    # 4 = DPLL_HOLDOVER
    locked = frozenset({2, 3})
    def prepare(self, rows):
        return super().prepare([
            r._replace(terror=float(r.terror)) for r in rows
        ])
