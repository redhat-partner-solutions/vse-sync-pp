### SPDX-License-Identifier: GPL-2.0-or-later

"""Filter log messages from multiple collectors"""

from argparse import ArgumentParser

import json

from decimal import Decimal

from .common import (
    open_input,
    JsonEncoder,
)

from .parsers import gnss
from .parsers import dpll

PARSERS = {
    cls.id_: cls for cls in (
        dpll.TimeErrorParser,
        gnss.TimeErrorParser,
    )
}

def filter_by_id(file, parser):
    """Filter lines from `file` object and send them to `parser`.
    `id_` is the value of the corresponding parser attribute; 

    Return the filtered parsed data in canonical form produced by the
    selected parser.
    """
    for line in file:
        obj = json.loads(line, parse_float=Decimal)
        if obj['id'] == parser.id_:
            yield parser.make_parsed(obj['data'])

def main():
    """Filter data from input to stdout as lines of JSON.
    
    The output written to stdout is parsed data from one filter
    specified in `parser` equivalent to a parser id. Each line written
    to stdout is parsed data conforming to the canonical form produced
    by the selected parser.
    """
    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        'input',
        help="collector file to parse, or '-' to read from stdin",
    )
    aparser.add_argument(
        'parser', choices=tuple(PARSERS),
        help="filtered data to parse from the collector file",
    )
    args = aparser.parse_args()
    parser = PARSERS[args.parser]()
    with open_input(args.input) as fid:
        for filtered in filter_by_id(fid, parser=parser):
            print(json.dumps(filtered, cls=JsonEncoder))

if __name__ == '__main__':
    main()
