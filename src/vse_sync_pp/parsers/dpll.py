### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse dpll log messages"""

from collections import namedtuple
from decimal import (Decimal, InvalidOperation)

from .parser import Parser

class TimeErrorParser(Parser):
    """Parse phase offset from a dpll CSV sample"""
    id_ = 'dpll/phase-offset'
    elems = ('timestamp', 'eecstate', 'phasestate', 'phaseoffset')
    y_name = 'phaseoffset'
    parsed = namedtuple('Parsed', elems)
    def make_parsed(self, elems):
        if len(elems) != len(self.elems):
            raise ValueError(elems)
        try:
            timestamp = Decimal(elems[0])
        except InvalidOperation as exc:
            raise ValueError(elems[0]) from exc
        try:
            phaseoffset = Decimal(elems[3])
        except InvalidOperation as exc:
            raise ValueError(elems[3]) from exc
        eecstate = int(elems[1])
        phasestate = int(elems[2])
        return self.parsed(timestamp, eecstate, phasestate, phaseoffset)
    def parse_line(self, line):
        # DPLL samples come from a fixed format CSV file
        return self.make_parsed(line.split(','))
