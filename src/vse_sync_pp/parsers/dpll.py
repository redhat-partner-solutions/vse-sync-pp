### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse dpll samples"""

from collections import namedtuple
from decimal import (Decimal, InvalidOperation)

class PhaseOffset():
    """Parse time offset from a dpll sample"""
    id_ = 'dpll/phase-offset'
    elems = ('timestamp', 'eecstate', 'phasestate', 'phaseoffset')
    parsed = namedtuple('Parsed', elems)
    def parse(self, line):
        """Parse phase offset from `line`.

        On success, return a :attr:`parsed` tuple.
        Otherwise, raise :class:`ValueError`.
        """
        # DPLL samples come from a fixed format CSV file
        elems = line.split(',')
        if len(elems) != 4:
            raise ValueError(line)
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
