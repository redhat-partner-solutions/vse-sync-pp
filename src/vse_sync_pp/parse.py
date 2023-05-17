### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse log messages"""

from argparse import ArgumentParser

import json

from .common import open_input

from .parsers.parser import JsonEncoder
from .parsers import dpll
from .parsers import ts2phc

PARSERS = {
    cls.id_: cls for cls in (
        dpll.PhaseOffset,
        ts2phc.TimeOffset,
    )
}

def main():
    """Print data parsed from log messages to stdout as lines of JSON"""
    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        '-r', '--relative', action='store_true',
        help="print timestamps relative to the first line's timestamp",
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
    with open_input(args.input) as fid:
        for parsed in parser.parse(fid, relative=args.relative):
            print(json.dumps(parsed, cls=JsonEncoder))

if __name__ == '__main__':
    main()
