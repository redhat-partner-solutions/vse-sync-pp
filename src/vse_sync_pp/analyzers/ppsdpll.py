### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze ppsdpll log messages"""
import numpy as np
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

class MovingAverageEmpty(Exception):
    """Moving Average data should be already calculated"""
    # empty

class PhaseOffsetConstantTimeErrorAnalyzer(Analyzer):
    """Analyze DPLL phase offset constant time error"""
    id_ = 'ppsdpll/phase-offset-constant-time-error'
    parser = 'dpll/phase-offset'
    cols = ('phaseoffset',)
    mov_avg = None
    def moving_average_lpf(self, data, window_size):
        """Calculate moving average low pass filter with `window_size`"""
        last = len(data)
        self.mov_avg = data.copy()
        for i in range(0, (last - window_size)):
            avg = np.mean(data[i : i + window_size])
            self.mov_avg[i] = avg
    def prepare(self, rows):
        return ((float(r[0]),) for r in rows)
    def test(self, data):
        self.moving_average_lpf(data.phaseoffset, 100)
        cto_min = self.mov_avg.min()
        cto_max = self.mov_avg.max()
        return max(abs(cto_min), abs(cto_max)) < 40
    def explain(self, data):
        if self.mov_avg is None:
            raise MovingAverageEmpty()
        cto_min = self.mov_avg.min()
        cto_max = self.mov_avg.max()
        return {
            'units': 'ns',
            'min': cto_min,
            'max': cto_max,
            'range': cto_max - cto_min,
            'mean': self.mov_avg.mean(),
            'stddev': self.mov_avg.std(),
            'variance': self.mov_avg.var(),
        }
