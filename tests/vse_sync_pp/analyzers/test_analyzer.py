### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers"""

from nose2.tools import params

from vse_sync_pp.analyzers.analyzer import CollectionIsClosed

from .. import make_fqname

class AnalyzerTestBuilder(type):
    """Build tests for vse_sync_pp.analyzers

    Specify this class as metaclass and provide:
    `constructor` - a callable returning the analyzer to test
    `id_` - the expected value of analyzer class attribute `id_`
    `parser` - the expected value of analyzer class attribute `parser`
    `expect` - a sequence of 3-tuples (rows, result, analysis) the analyzer must
               produce
    """
    def __new__(cls, name, bases, dct): # pylint: disable=bad-mcs-classmethod-argument
        constructor = dct['constructor']
        fqname = make_fqname(constructor)
        dct.update({
            'test_id': cls.make_test_id(
                constructor, fqname,
                dct['id_'],
            ),
            'test_parser': cls.make_test_parser(
                constructor, fqname,
                dct['parser'],
            ),
            'test_result': cls.make_test_result(
                constructor, fqname,
                dct['expect'],
            ),
        })
        return super().__new__(cls, name, bases, dct)
    # make functions for use as TestCase methods
    @staticmethod
    def make_test_id(constructor, fqname, id_):
        """Make a function testing id_ class attribute value"""
        def method(self):
            """Test analyzer id_ class attribute value"""
            self.assertEqual(constructor.id_, id_)
        method.__doc__ = f'Test {fqname} id_ class attribute value'
        return method
    @staticmethod
    def make_test_parser(constructor, fqname, parser):
        """Make a function testing parser class attribute value"""
        def method(self):
            """Test analyzer parser class attribute value"""
            self.assertEqual(constructor.parser, parser)
        method.__doc__ = f'Test {fqname} parser class attribute value'
        return method
    @staticmethod
    def make_test_result(constructor, fqname, expect):
        """Make a function testing analyzer test result and analysis"""
        @params(*expect)
        def method(self, rows, result, analysis):
            """Test analyzer produces `result` and `analysis` for `rows`"""
            analyzer = constructor()
            analyzer.collect(*rows)
            self.assertEqual(analyzer.result, result)
            self.assertEqual(analyzer.analysis, analysis)
            with self.assertRaises(CollectionIsClosed):
                analyzer.collect(*rows)
            self.assertEqual(analyzer.result, result)
            self.assertEqual(analyzer.analysis, analysis)
        method.__doc__ = f'Test {fqname} analyzer test result and analysis'
        return method
