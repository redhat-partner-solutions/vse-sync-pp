### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ppsdpll log messages"""

from .analyzer import Analyzer

class TimeErrorAnalyzer(Analyzer):
    """Analyze DPLL phase offset time error"""
    id_ = 'ppsdpll/time-error'
    parser = 'dpll/time-error'
    def __init__(self, config):
        super().__init__(config)
        # required system time output accuracy
        accuracy = config.requirement('time-error-in-locked-mode/ns')
        # limit on inaccuracy at observation point
        limit = config.parameter('time-error-limit/%')
        # exclusive upper bound on absolute time error for any sample
        self._unacceptable = accuracy * limit / 100
        # samples in the initial transient period are ignored
        self._transient = config.parameter('transient-period/s')
        # minimum test duration for a valid test
        self._duration = config.parameter('min-test-duration/s')
    def prepare(self, rows):
        return super().prepare([
            r._replace(phaseoffset=float(r.phaseoffset)) for r in rows
        ])
    def test(self, data):
        if len(data) == 0:
            return (False, "no data")
        pho_min = data.phaseoffset.min()
        pho_max = data.phaseoffset.max()
        if self._unacceptable <= max(abs(pho_min), abs(pho_max)):
            return (False, "unacceptable time error")
        if data.iloc[-1].timestamp - data.iloc[0].timestamp < self._duration:
            return (False, "short test duration")
        if len(data) - 1 < self._duration:
            return (False, "short test samples")
        return (True, None)
    def explain(self, data):
        if len(data) == 0:
            return {}
        return {
            'duration': data.iloc[-1].timestamp - data.iloc[0].timestamp,
            'phaseoffset': self._statistics(data.phaseoffset, 'ns'),
        }
