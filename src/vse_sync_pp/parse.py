### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse log messages"""

from argparse import ArgumentParser
import sys
from contextlib import nullcontext

import json
from decimal import Decimal

from .parsers import ts2phc

PARSERS = {
    cls.id_: cls for cls in (
        ts2phc.TimeError,
    )
}

class DecimalEncoder(json.JSONEncoder):
    """A JSON encoder accepting :class:`Decimal` values"""
    def default(self, o):
        """Return a commonly serializable value from `o`"""
        if isinstance(o, Decimal):
            return float(o)
        return super(o)

def main():
    """Print data parsed from log messages to stdout as lines of JSON"""
    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        '--elems', action='store_true',
        help="print data element names as the first line"
    )
    aparser.add_argument(
        'input',
        help="log file to parse, or '-' to read from stdin",
    )
    aparser.add_argument(
        'parser', choices=tuple(PARSERS),
        help="data to parse from the log file",
    )
    args = aparser.parse_args()
    parser = PARSERS[args.parser]()
    with (  open(args.input, encoding='utf-8')
            if args.input != '-' else
            nullcontext(sys.stdin)
        ) as fid:
        if args.elems:
            print(json.dumps(parser.elems))
        for line in fid:
            parsed = parser.parse(line)
            if parsed is not None:
                print(json.dumps(parsed, cls=DecimalEncoder))

if __name__ == '__main__':
    main()
