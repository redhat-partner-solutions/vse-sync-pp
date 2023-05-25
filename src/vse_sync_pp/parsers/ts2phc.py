### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse ts2phc log messages"""

import re
from collections import namedtuple
from decimal import Decimal

from .parser import Parser

class TimeErrorParser(Parser):
    """Parse time error from a ts2phc log message"""
    id_ = 'ts2phc/time-error'
    elems = ('timestamp', 'interface', 'terror', 'state')
    y_name = 'terror'
    parsed = namedtuple('Parsed', elems)
    @staticmethod
    def build_regexp(interface=None):
        """Return a regular expression string for parsing log file lines.

        If `interface` then only parse lines for the specified interface.
        """
        return r'\s'.join((
            r'^ts2phc' +
            r'\[([1-9][0-9]*\.[0-9]{3})\]:', # timestamp
            r'\[ts2phc\.0\..*\]',
            fr'({interface})' if interface else r'(\S+)', # interface
            r'master offset\s*',
            r'(-?[0-9]+)', # time error
            r'(\S+)', # state
            r'.*$',
        ))
    def __init__(self, interface=None):
        super().__init__()
        self._regexp = re.compile(self.build_regexp(interface))
    def make_parsed(self, elems):
        if len(elems) != len(self.elems):
            raise ValueError(elems)
        return self.parsed(
            Decimal(elems[0]),
            str(elems[1]),
            int(elems[2]),
            str(elems[3]),
        )
    def parse_line(self, line):
        matched = self._regexp.match(line)
        if matched:
            return self.make_parsed((
                matched.group(1),
                matched.group(2),
                matched.group(3),
                matched.group(4),
            ))
        return None
