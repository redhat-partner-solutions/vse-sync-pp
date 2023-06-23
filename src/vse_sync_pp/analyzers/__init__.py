### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyzers"""

from .analyzer import Config

from . import (
    gnss,
    ppsdpll,
    ts2phc,
)

ANALYZERS = {
    cls.id_: cls for cls in (
        gnss.TimeErrorAnalyzer,
        ppsdpll.TimeErrorAnalyzer,
        ts2phc.TimeErrorAnalyzer,
    )
}
