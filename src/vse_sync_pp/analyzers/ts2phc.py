### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ts2phc log messages"""

from .analyzer import TimeErrorAnalyzer

class Ts2PhcAnalyzer(TimeErrorAnalyzer):
    """Analyze time error"""
    id_ = 'ts2phc/time-error'
    parser = id_
    def __init__(self, config):
        super().__init__(config)
    def prepare(self, rows):
        idx = 0
        try:
            tstart = rows[0].timestamp + self._transient
        except IndexError:
            pass
        else:
            while idx < len(rows):
                if tstart <= rows[idx].timestamp:
                    break
                idx += 1
        return super().prepare(rows[idx:])
