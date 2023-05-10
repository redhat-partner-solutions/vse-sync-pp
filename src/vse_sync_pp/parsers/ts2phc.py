### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse ts2phc log messages"""

import re
from collections import namedtuple
from decimal import Decimal

class TimeOffset():
    """Parse time offset from a ts2phc log message"""
    id_ = 'ts2phc/time-offset'
    elems = ('timestamp', 'interface', 'toffset', 'state')
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
            r'(-?[0-9]+)', # time offset
            r'(\S+)', # state
            r'.*$',
        ))
    def __init__(self, interface=None):
        self._regexp = re.compile(self.build_regexp(interface))
    def parse(self, line):
        """Parse time offset from `line`.

        On success, return a :attr:`parsed` tuple. Otherwise, return None.
        """
        matched = self._regexp.match(line)
        if matched:
            return self.parsed(
                Decimal(matched.group(1)),
                matched.group(2),
                int(matched.group(3)),
                matched.group(4),
            )
        return None
