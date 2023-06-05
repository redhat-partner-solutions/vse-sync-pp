### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ppsdpll log messages"""

from .analyzer import TimeErrorAnalyzerBase

class TimeErrorAnalyzer(TimeErrorAnalyzerBase):
    """Analyze DPLL time error"""
    id_ = 'ppsdpll/time-error'
    parser = 'dpll/time-error'
    locked = frozenset({3})
    def prepare(self, rows):
        return super().prepare([
            r._replace(terror=float(r.terror)) for r in rows
        ])
