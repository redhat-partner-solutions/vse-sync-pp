### SPDX-License-Identifier: GPL-2.0-or-later

"""Plot data parsed from log messages from a single source."""

from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt

from .common import open_input

from .parsers import PARSERS

class Plotter():
    """Rudimentary plotter of data values against timestamp"""
    def __init__(self, y_name):
        self._x_name = 'timestamp'
        self._y_name = y_name
        self._x_data = []
        self._y_data = []
    def append(self, data):
        """Append x and y data points extracted from `data`"""
        x_val = getattr(data, self._x_name)
        self._x_data.append(x_val)
        y_val = getattr(data, self._y_name)
        self._y_data.append(y_val)
    def plot(self, filename):
        """Plot data to `filename`"""
        fig, (ax1, ax2) = plt.subplots(2, constrained_layout=True)
        fig.set_size_inches(10, 8)
        ax1.axhline(0, color='black')
        if any((abs(v) > 10 for v in self._y_data)):
            ax1.set_yscale('symlog', linthresh=10)
        ax1.plot(self._x_data, self._y_data, '.')
        ax1.grid()
        ax1.set_title(f'{self._x_name} vs {self._y_name}')
        counts, bins = np.histogram(
            np.array(self._y_data, dtype=float),
            bins='scott',
        )
        ax2.hist(bins[:-1], bins, weights=counts)
        ax2.set_yscale('symlog', linthresh=10)
        ax2.set_title(f'Histogram of {self._y_name}')
        plt.savefig(filename)

def main():
    """Plot data parsed from log messages from a single source.

    Plot data parsed from the log messages in input to an image file.
    """
    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        '-c', '--canonical', action='store_true',
        help="input contains canonical data",
    )
    aparser.add_argument(
        'input',
        help="input file, or '-' to read from stdin",
    )
    aparser.add_argument(
        'parser', choices=tuple(PARSERS),
        help="data to parse from input",
    )
    aparser.add_argument(
        'output',
        help="output image filename",
    )
    args = aparser.parse_args()
    parser = PARSERS[args.parser]()
    plotter = Plotter(parser.y_name)
    with open_input(args.input) as fid:
        method = parser.canonical if args.canonical else parser.parse
        for parsed in method(fid):
            plotter.append(parsed)
    plotter.plot(args.output)

if __name__ == '__main__':
    main()
