### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ts2phc log messages"""

from pandas import concat

from .analyzer import Analyzer

class TimeErrorAnalyzer(Analyzer):
    """Analyze time error"""
    id_ = 'ts2phc/time-error'
    parser = id_
    cols = ('timestamp', 'interface', 'terror', 'state')
    def __init__(self, config):
        super().__init__(config)
        # required whole system time output accuracy
        accuracy = config.requirement('time-error-in-locked-mode/ns')
        # tolerated time output inaccuracy at observation point
        limit = config.parameter('time-error-limit/%')
        # bounds on absolute time error for any sample
        self._unacceptable = accuracy * limit / 100
        # samples in the initial transient period are ignored
        self._transient = config.parameter('transient-period/s')
        # minimum test duration for a valid test
        self._duration = config.parameter('min-test-duration/s')
    def prepare(self, rows):
        tstart = rows[0][0] + self._transient
        idx = 0
        while idx < len(rows):
            if tstart <= rows[idx][0]:
                break
            idx += 1
        return rows[idx:]
    def test(self, data):
        # reject if any sample has unacceptable time error
        terr_min = data.terror.min()
        terr_max = data.terror.max()
        if self._unacceptable <= max(abs(terr_min), abs(terr_max)):
            return False
        # reject if test duration is too short
        if data.iloc[-1].timestamp - data.iloc[0].timestamp < self._duration:
            return False
        # reject if too few samples received (assume 1 sample per second)
        if len(data) < self._duration:
            return False
        return True
    def explain(self, data):
        terr_min = data.terror.min()
        terr_max = data.terror.max()
        return {
            'duration': data.iloc[-1].timestamp - data.iloc[0].timestamp,
            'min': terr_min,
            'max': terr_max,
            'range': terr_max - terr_min,
            'mean': data.terror.mean(),
            'stddev': data.terror.std(),
            'variance': data.terror.var(),
        }
