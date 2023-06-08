### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse GNSS log messages"""

from collections import namedtuple
from decimal import (Decimal, InvalidOperation)

from .parser import Parser

class TimeErrorParser(Parser):
    """Parse time error from a GNSS CSV sample"""
    id_ = 'gnss/time-error'
    elems = ('timestamp', 'state', 'terror')
    ### TODO: define state mappings
    y_name = 'terror'
    parsed = namedtuple('Parsed', elems)
    def make_parsed(self, elems):
        if len(elems) != len(self.elems):
            raise ValueError(elems)
        try:
            timestamp = Decimal(elems[0])
        except InvalidOperation as exc:
            raise ValueError(elems[0]) from exc
        return self.parsed(
            timestamp,
            int(elems[1]),
            int(elems[2]),
        )
    def parse_line(self, line):
        # GNSS samples come from a fixed format CSV file
        return self.make_parsed(line.split(','))
