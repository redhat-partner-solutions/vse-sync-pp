### SPDX-License-Identifier: GPL-2.0-or-later

"""Common analyzer functionality"""

import yaml
from pandas import DataFrame
from datetime import (datetime, timezone)

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
        self._timestamp = None
        self._duration = None
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
    def _explain(self):
        """Close data collection and explain collected data"""
        if self._analysis is None:
            self.close()
            self._analysis = self.explain(self._data)
            self._timestamp = self._analysis.pop('timestamp', None)
            self._duration = self._analysis.pop('duration', None)
    def _timestamp_from_dec(self, dec):
        """Return an absolute timestamp or decimal timestamp from `dec`.

        If `dec` is large enough to represent 2023 (the year this was coded),
        or a later year, then assume it represents an absolute date-time. (This
        is >53 years if counting seconds from zero.) Otherwise assume relative
        time.

        >>> today = datetime.now()
        >>> today
        datetime.datetime(2023, 9, 8, 16, 49, 54, 735285)
        >>> ts = today.timestamp()
        >>> ts
        1694188194.735285
        >>> ts / (365 * 24 * 60 * 60)
        53.72235523640554
        """
        # `dtv` is a timezone-aware datetime value with resolution of seconds
        dtv = datetime.fromtimestamp(int(dec), tz=timezone.utc)
        if datetime.now().year - dtv.year <= 1:
            # absolute date-time
            return dtv.isoformat()
        # relative time
        return dec
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
    def timestamp(self):
        """The ISO 8601 date-time timestamp, when the test started"""
        self._explain()
        return self._timestamp
    @property
    def duration(self):
        """The test duration in seconds"""
        self._explain()
        return self._duration
    @property
    def analysis(self):
        """A structured analysis of the collected data"""
        self._explain()
        return self._analysis
    @staticmethod
    def _statistics(data, units, ndigits=3):
        """Return a dict of statistics for `data`, rounded to `ndigits`"""
        def _round(val):
            """Return `val` as native Python type or Decimal, rounded to `ndigits`"""
            try:
                return round(val.item(), ndigits)
            except AttributeError:
                return round(val, ndigits)
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

class TimeErrorAnalyzerBase(Analyzer):
    """Analyze time error.

    Derived classes must override class attribute `locked`, specifying a
    frozenset of values representing locked states.
    """
    locked = frozenset()
    def __init__(self, config):
        super().__init__(config)
        # required system time output accuracy
        accuracy = config.requirement('time-error-in-locked-mode/ns')
        # limit on inaccuracy at observation point
        limit = config.parameter('time-error-limit/%')
        # exclusive upper bound on absolute time error for any sample
        self._unacceptable = accuracy * (limit / 100)
        # samples in the initial transient period are ignored
        self._transient = config.parameter('transient-period/s')
        # minimum test duration for a valid test
        self._duration_min = config.parameter('min-test-duration/s')
    def prepare(self, rows):
        idx = 0
        try:
            tstart = rows[0].timestamp + self._transient
        except IndexError:
            pass
        else:
            while idx < len(rows):
                if tstart <= rows[idx].timestamp:
                    break
                idx += 1
        return super().prepare(rows[idx:])
    def test(self, data):
        if len(data) == 0:
            return (False, "no data")
        if frozenset(data.state.unique()).difference(self.locked): # pylint: disable=no-member
            return (False, "loss of lock")
        terr_min = data.terror.min()
        terr_max = data.terror.max()
        if self._unacceptable <= max(abs(terr_min), abs(terr_max)):
            return (False, "unacceptable time error")
        if data.iloc[-1].timestamp - data.iloc[0].timestamp < self._duration_min:
            return (False, "short test duration")
        if len(data) - 1 < self._duration_min:
            return (False, "short test samples")
        return (True, None)
    def explain(self, data):
        if len(data) == 0:
            return {}
        return {
            'timestamp': self._timestamp_from_dec(data.iloc[0].timestamp),
            'duration': data.iloc[-1].timestamp - data.iloc[0].timestamp,
            'terror': self._statistics(data.terror, 'ns'),
        }
