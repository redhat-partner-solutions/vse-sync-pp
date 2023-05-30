### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ppsdpll log messages"""

from .analyzer import Analyzer

class PhaseOffsetTimeErrorAnalyzer(Analyzer):
    """Analyze DPLL phase offset time error"""
    id_ = 'ppsdpll/phase-offset-time-error'
    parser = 'dpll/phase-offset'
    def __init__(self, config):
        super().__init__(config)
        # required system time output accuracy
        accuracy = config.requirement('time-error-in-locked-mode/ns')
        # exclusive upper bound on absolute time error for any sample
        self._unacceptable = accuracy
    def prepare(self, rows):
        return super().prepare([
            r._replace(phaseoffset=float(r.phaseoffset)) for r in rows
        ])
    def test(self, data):
        pho_min = data.phaseoffset.min()
        pho_max = data.phaseoffset.max()
        if self._unacceptable <= max(abs(pho_min), abs(pho_max)):
            return False
        return True
    def explain(self, data):
        pho_min = data.phaseoffset.min()
        pho_max = data.phaseoffset.max()
        return {
            'units': 'ns',
            'min': pho_min,
            'max': pho_max,
            'range': pho_max - pho_min,
            'mean': data.phaseoffset.mean(),
            'stddev': data.phaseoffset.std(),
            'variance': data.phaseoffset.var(),
        }
