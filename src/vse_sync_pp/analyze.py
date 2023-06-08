### SPDX-License-Identifier: GPL-2.0-or-later

"""Analyze log messages"""

import json
from argparse import ArgumentParser

from .common import (
    open_input,
    JsonEncoder,
)

from .parse import PARSERS

from .analyzers.analyzer import Config
from .analyzers import (
    gnss,
    ppsdpll,
    ts2phc,
)

ANALYZERS = {
    cls.id_: cls for cls in (
        gnss.TimeErrorAnalyzer,
        ppsdpll.TimeErrorAnalyzer,
        ts2phc.TimeErrorAnalyzer,
    )
}

def main():
    """Print test analysis of data parsed from log messages to stdout"""
    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        '--canonical', action='store_true',
        help="parse canonical log data from input",
    )
    aparser.add_argument(
        '--config',
        help="YAML file specifying test requirements and parameters",
    )
    aparser.add_argument(
        'input',
        help="data parsed or '-' to read from stdin",
    )
    aparser.add_argument(
        'analyzer', choices=tuple(ANALYZERS),
        help="analyzer to run",
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
