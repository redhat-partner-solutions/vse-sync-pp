### SPDX-License-Identifier: GPL-2.0-or-later

"""Parse log messages from a single source."""

from argparse import ArgumentParser

import json

from .common import (
    open_input,
    JsonEncoder,
)

from .parsers import PARSERS

def main():
    """Parse log messages from a single source.

    Parse log messages using the specified parser. For each parsed log message
    print the canonical data produced by the parser as JSON.
    """
    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        '-r', '--relative', action='store_true',
        help="print timestamps relative to the first line's timestamp",
    )
    aparser.add_argument(
        'input',
        help="input file, or '-' to read from stdin",
    )
    aparser.add_argument(
        'parser', choices=tuple(PARSERS),
        help="data to parse from input",
    )
    args = aparser.parse_args()
    parser = PARSERS[args.parser]()
    with open_input(args.input) as fid:
        for data in parser.parse(fid, relative=args.relative):
            print(json.dumps(data, cls=JsonEncoder))

if __name__ == '__main__':
    main()
