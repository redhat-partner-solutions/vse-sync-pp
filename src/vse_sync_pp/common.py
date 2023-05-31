### SPDX-License-Identifier: GPL-2.0-or-later

"""Common code for command line tools"""

import sys
from contextlib import nullcontext

import json
from decimal import Decimal

def open_input(filename, encoding='utf-8', **kwargs):
    """Return a context manager for reading from `filename`.

    If `filename` is '-' then read from stdin instead of `filename`.
    """
    if filename == '-':
        return nullcontext(sys.stdin)
    return open(filename, encoding=encoding, **kwargs)

class JsonEncoder(json.JSONEncoder):
    """A JSON encoder accepting :class:`Decimal` values"""
    def default(self, o):
        """Return a commonly serializable value from `o`"""
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)
