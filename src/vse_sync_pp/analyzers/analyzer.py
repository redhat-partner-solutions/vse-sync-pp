### SPDX-License-Identifier: GPL-2.0-or-later

"""Common analyzer functionality"""

from operator import attrgetter

from pandas import DataFrame

class CollectionIsClosed(Exception):
    """Data Collection has been closed while collecting data"""
    # empty

class Analyzer():
    """A base class providing common analyzer functionality

    Derived classes must override class attribute `cols`, specifying a
    list of column names to extract from collected rows of data.
    """
    cols = ()
    def __init__(self):
        getter = attrgetter(*self.cols)
        if len(self.cols) > 1:
            self._row_builder = getter
        else:
            self._row_builder = lambda row: (getter(row),)
        self._rows = []
        self._data = None
    def collect(self, *rows):
        """Collect data from `rows`"""
        if self._rows is None:
            raise CollectionIsClosed()
        self._rows.extend([self._row_builder(r) for r in rows])
    def prepare(self, rows): # pylint: disable=no-self-use
        """Return collected data `rows` prepared for test and analysis"""
        return rows
    def close(self):
        """Close data collection"""
        if self._data is None:
            records = self.prepare(self._rows)
            self._data = DataFrame.from_records(records, columns=self.cols)
            self._rows = None
    @property
    def result(self):
        """Return True if collected data passes this analyzer's test"""
        self.close()
        return self.test(self._data)
    @property
    def analysis(self):
        """Return a machine-readable analysis of the collected data"""
        self.close()
        return self.explain(self._data)
    def test(self, data):
        """A boolean function testing if `data` passes this analyzer"""
        raise NotImplementedError
    def explain(self, data):
        """Return a machine-readable analysis of `data`"""
        raise NotImplementedError
