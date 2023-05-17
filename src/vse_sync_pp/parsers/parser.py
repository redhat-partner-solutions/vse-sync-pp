### SPDX-License-Identifier: GPL-2.0-or-later

"""Common parser functionality"""

import json
from decimal import Decimal

class JsonEncoder(json.JSONEncoder):
    """A JSON encoder accepting :class:`Decimal` values"""
    def default(self, o):
        """Return a commonly serializable value from `o`"""
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)

class Parser():
    """A base class providing common parser functionality"""
    def make_parsed(self, elems): # pylint: disable=no-self-use
        """Return a namedtuple value from parsed iterable `elems`.

        Raise :class:`ValueError` if a value cannot be formed from `elems`.
        """
        raise ValueError(elems)
    def parse_line(self, line): # pylint: disable=no-self-use,unused-argument
        """Parse `line`.

        If `line` is accepted, return a namedtuple value.
        If `line` is rejected, raise :class:`ValueError`.
        Otherwise the `line` is discarded, return None.
        """
        return None
    def parse(self, file, relative=False):
        """Parse lines from `file` object.

        This method is a generator yielding a namedtuple value for each
        accepted line in `file`. If `relative` is truthy, then present all
        timestamps relative to the first accepted line's timestamp.
        """
        tzero = None
        for line in file:
            parsed = self.parse_line(line) # pylint: disable=assignment-from-none
            if parsed is not None:
                if relative:
                    timestamp = getattr(parsed, 'timestamp', None)
                    if timestamp is not None:
                        if tzero is None:
                            tzero = timestamp
                        parsed = parsed._replace(timestamp=timestamp - tzero)
                yield parsed
    def canonical(self, file):
        """Parse canonical data from `file` object.

        The canonical representation is JSON-encoded parsed data, with one
        parsed item per line in `file`.

        This method is a generator yielding a namedtuple value for each line in
        `file`.
        """
        for line in file:
            obj = json.loads(line, parse_float=Decimal)
            yield self.make_parsed(obj)
