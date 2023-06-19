### SPDX-License-Identifier: GPL-2.0-or-later

"""Common parser functionality"""

import json
import re
from datetime import (datetime, timezone)
from decimal import (Decimal, InvalidOperation)

# sufficient regex to extract the whole decimal fraction part
RE_ISO8601_DECFRAC = re.compile(
    r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\.(\d+)(.*)$'
)

def parse_timestamp_abs(val):
    """Return a :class:`Decimal` from `val`, an absolute timestamp string.

    Accepted absolute timestamp strings are ISO 8601 format with restrictions.
    The string must: explicitly specify UTC timezone, supply time in seconds,
    specify a decimal fractional part with a decimal mark of '.'.

    Return None if `val` is not a string or is not an ISO 8601 format string.
    Raise :class:`ValueError` otherwise.
    """
    try:
        dtv = datetime.fromisoformat(val)
    except TypeError:
        return None
    except ValueError:
        # before Python 3.11 `fromisoformat` fails if UTC denoted by 'Z' and/or
        # the decimal fraction has more than 6 digits
        match = RE_ISO8601_DECFRAC.match(val)
        if match is None:
            return None
        # parse without decimal fraction, with 'Z' substituted
        dtv = datetime.fromisoformat(
            val.group(1) + '+00:00' if val.group(3) == 'Z' else val.group(3)
        )
    else:
        match = RE_ISO8601_DECFRAC.match(val)
        if match is None:
            raise ValueError(val)
    if dtv.tzinfo != timezone.utc:
        raise ValueError(val)
    return Decimal(f'{int(dtv.timestamp())}.{match.group(2)}')

def parse_decimal(val):
    """Return a :class:`Decimal` from `val` or raise :class:`ValueError`"""
    try:
        return Decimal(val)
    except InvalidOperation as exc:
        raise ValueError(val) from exc

def parse_timestamp(val):
    """Return a :class:`Decimal` from absolute or relative timestamp `val`"""
    return parse_timestamp_abs(val) or parse_decimal(val)

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
