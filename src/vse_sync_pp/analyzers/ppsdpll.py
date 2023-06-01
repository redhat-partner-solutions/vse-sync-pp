### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ppsdpll log messages"""

from .analyzer import TimeErrorAnalyzer

class PpsDpllAnalyzer(TimeErrorAnalyzer):
    """Analyze DPLL phase offset time error"""
    id_ = 'ppsdpll/time-error'
    parser = 'dpll/time-error'
    def __init__(self, config):
        super().__init__(config)
        self._lockid = {3}
    def prepare(self, rows):
        return super().prepare([
            r._replace(terror=float(r.terror)) for r in rows
        ])
