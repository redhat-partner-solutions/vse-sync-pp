### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ts2phc log messages"""

from .analyzer import Analyzer

class TimeErrorAnalyzer(Analyzer):
    """Analyze time error"""
    id_ = 'ts2phc/time-error'
    parser = id_
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
        tstart = rows[0].timestamp + self._transient
        idx = 0
        while idx < len(rows):
            if tstart <= rows[idx].timestamp:
                break
            idx += 1
        return super().prepare(rows[idx:])
    def test(self, data):
        if len(data) == 0:
            return (False, "no data")
        if frozenset(data.state.unique()) != {'s2'}:
            return (False, "loss of lock")
        terr_min = data.terror.min()
        terr_max = data.terror.max()
        if self._unacceptable <= max(abs(terr_min), abs(terr_max)):
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
            'terror': self._statistics(data.terror, 'ns'),
        }
