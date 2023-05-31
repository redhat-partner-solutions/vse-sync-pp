### SPDX-License-Identifier: GPL-2.0-or-later

"""Common analyzer functionality"""

import yaml

from pandas import DataFrame

from ..requirements import REQUIREMENTS

class Config():
    """Analyzer configuration"""
    def __init__(self, filename=None, requirements=None, parameters=None):
        self._filename = filename
        self._requirements = requirements
        self._parameters = parameters
    def _reason(self, reason):
        """Return `reason`, extended if this config is from a file."""
        if self._filename is None:
            return reason
        return reason + f' in config file {self._filename}'
    def requirement(self, key):
        """Return the value at `key` in this configuration's requirements.

        Raise :class:`KeyError` if a value cannot be returned.
        """
        try:
            return REQUIREMENTS[self._requirements][key]
        except KeyError as exc:
            if self._requirements is None:
                reason = 'no requirements specified'
            elif self._requirements not in REQUIREMENTS:
                reason = f'unknown requirements {self._requirements}'
            else:
                reason = f'unknown requirement {key} in {self._requirements}'
            raise KeyError(self._reason(reason)) from exc
    def parameter(self, key):
        """Return the value at `key` in this configuration's parameters.

        Raise :class:`KeyError` if a value cannot be returned.
        """
        try:
            return self._parameters[key]
        except TypeError as exc:
            reason = 'no parameters specified'
            raise KeyError(self._reason(reason)) from exc
        except KeyError as exc:
            reason = f'unknown parameter {key}'
            raise KeyError(self._reason(reason)) from exc
    @classmethod
    def from_yaml(cls, filename, encoding='utf-8'):
        """Build configuration from YAML file at `filename`"""
        with open(filename, encoding=encoding) as fid:
            dct = dict(yaml.safe_load(fid.read()))
        return cls(filename, dct.get('requirements'), dct.get('parameters'))

class CollectionIsClosed(Exception):
    """Data collection was closed while collecting data"""
    # empty

class Analyzer():
    """A base class providing common analyzer functionality"""
    def __init__(self, config):
        self._config = config
        self._rows = []
        self._data = None
        self._result = None
        self._reason = None
        self._analysis = None
    def collect(self, *rows):
        """Collect data from `rows`"""
        if self._rows is None:
            raise CollectionIsClosed()
        self._rows += rows
    def prepare(self, rows): # pylint: disable=no-self-use
        """Return (columns, records) from collected data `rows`

        `columns` is a sequence of column names
        `records` is a sequence of rows prepared for test analysis

        If `records` is an empty sequence, then `columns` is also empty.
        """
        return (rows[0]._fields, rows) if rows else ((), ())
    def close(self):
        """Close data collection"""
        if self._data is None:
            (columns, records) = self.prepare(self._rows)
            self._data = DataFrame.from_records(records, columns=columns)
            self._rows = None
    def _test(self):
        """Close data collection and test collected data"""
        if self._result is None:
            self.close()
            (self._result, self._reason) = self.test(self._data)
    @property
    def result(self):
        """The boolean result from this analyzer's test of the collected data"""
        self._test()
        return self._result
    @property
    def reason(self):
        """A string qualifying :attr:`result` (or None if unqualified)"""
        self._test()
        return self._reason
    @property
    def analysis(self):
        """A structured analysis of the collected data"""
        if self._analysis is None:
            self.close()
            self._analysis = self.explain(self._data)
        return self._analysis
    @staticmethod
    def _statistics(data, units, ndigits=3):
        """Return a dict of statistics for `data`, rounded to `ndigits`"""
        def _round(val):
            """Return `val` as native Python type, rounded to `ndigits`"""
            return round(val.item(), ndigits)
        min_ = data.min()
        max_ = data.max()
        return {
            'units': units,
            'min': _round(min_),
            'max': _round(max_),
            'range': _round(max_ - min_),
            'mean': _round(data.mean()),
            'stddev': _round(data.std()),
            'variance': _round(data.var()),
        }
    def test(self, data):
        """This analyzer's test of the collected `data`.

        Return a 2-tuple (result, reason). Boolean `result` indicates test
        pass/fail. String `reason` qualifies `result` (or None is `result`
        if unqualified).
        """
        raise NotImplementedError
    def explain(self, data):
        """Return a structured analysis of the collected `data`"""
        raise NotImplementedError
