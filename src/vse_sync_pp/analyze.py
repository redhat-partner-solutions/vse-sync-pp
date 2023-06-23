### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze log messages from a single source."""

import json
from argparse import ArgumentParser

from .common import (
    open_input,
    JsonEncoder,
)

from .parsers import PARSERS
from .analyzers import (
    ANALYZERS,
    Config,
)

def main():
    """Analyze log messages from a single source.

    Analyze data parsed from the log messages in input. Print the test result
    and data analysis as JSON.
    """
    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        '--canonical', action='store_true',
        help="input contains canonical data",
    )
    aparser.add_argument(
        '--config',
        help="YAML file specifying test requirements and parameters",
    )
    aparser.add_argument(
        'input',
        help="input file, or '-' to read from stdin",
    )
    aparser.add_argument(
        'analyzer', choices=tuple(ANALYZERS),
        help="analyzer to run over input",
    )
    args = aparser.parse_args()
    config = Config.from_yaml(args.config) if args.config else Config()
    analyzer = ANALYZERS[args.analyzer](config)
    parser = PARSERS[analyzer.parser]()
    with open_input(args.input) as fid:
        method = parser.canonical if args.canonical else parser.parse
        for parsed in method(fid):
            analyzer.collect(parsed)
    dct = {
        'result': analyzer.result,
        'reason': analyzer.reason,
        'analysis': analyzer.analysis,
    }
    print(json.dumps(dct, cls=JsonEncoder))

if __name__ == '__main__':
    main()
