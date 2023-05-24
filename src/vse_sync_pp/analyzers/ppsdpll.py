### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ppsdpll log messages"""

from .analyzer import Analyzer

### TODO
#prtc_b = 40
#prtc_a = 100

class PhaseOffsetTimeErrorAnalyzer(Analyzer):
    """Analyze DPLL phase offset time error"""
    id_ = 'ppsdpll/phase-offset-time-error'
    parser = 'dpll/phase-offset'
    cols = ('phaseoffset',)
    def prepare(self, rows):
        return ((float(r[0]),) for r in rows)
    def test(self, data):
        pho_min = data.phaseoffset.min()
        pho_max = data.phaseoffset.max()
        if max(abs(pho_min), abs(pho_max)) < 40:
            return True
        return False
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
