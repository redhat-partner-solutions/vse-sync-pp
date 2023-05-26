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
    """Data Collection has been closed while collecting data"""
    # empty

class Analyzer():
    """A base class providing common analyzer functionality"""
    def __init__(self, config):
        self._config = config
        self._rows = []
        self._data = None
    def collect(self, *rows):
        """Collect data from `rows`"""
        if self._rows is None:
            raise CollectionIsClosed()
        self._rows += rows
    def prepare(self, rows): # pylint: disable=no-self-use
        """Return (columns, records) from collected data `rows`

        `columns` is a sequence of column names
        `records` is a sequence of rows prepared for test analysis
        """
        return (rows[0]._fields, rows)
    def close(self):
        """Close data collection"""
        if self._data is None:
            (columns, records) = self.prepare(self._rows)
            self._data = DataFrame.from_records(records, columns=columns)
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
