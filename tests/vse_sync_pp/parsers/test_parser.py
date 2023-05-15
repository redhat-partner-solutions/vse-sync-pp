### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.parsers"""

from nose2.tools import params

from .. import make_fqname

class ParserTestBuilder(type):
    """Build tests for vse_sync_pp.parsers

    Specify this class as metaclass and provide:
    `constructor` - a callable returning the parser to test
    `id_` - the expected value of parser attribute `id_`
    `elems` - the expected value of parser attribute `elems`
    `accept` - a sequence of 2-tuples (line, expect) the parser must accept
    `reject` - a sequence of lines the parser must reject with ValueError
    `discard` - a sequence of lines the parser must discard
    """
    def __new__(cls, name, bases, dct):
        constructor = dct['constructor']
        fqname = make_fqname(constructor)
        dct.update({
            'test_id': cls.make_test_id(
                constructor, fqname,
                dct['id_'],
            ),
            'test_elems': cls.make_test_elems(
                constructor, fqname,
                dct['elems'],
            ),
            'test_accept': cls.make_test_accept(
                constructor, fqname,
                dct['elems'], dct['accept'],
            ),
            'test_reject': cls.make_test_reject(
                constructor, fqname,
                dct['reject'],
            ),
            'test_discard': cls.make_test_discard(
                constructor, fqname,
                dct['discard'],
            ),
        })
        return super().__new__(cls, name, bases, dct)
    # make functions for use as TestCase methods
    @staticmethod
    def make_test_id(constructor, fqname, id_):
        """Make a function testing id_ attribute value"""
        def method(self):
            """Test parser id_ attribute value"""
            parser = constructor()
            self.assertEqual(parser.id_, id_)
        method.__doc__ = f'Test {fqname} id_ attribute value'
        return method
    @staticmethod
    def make_test_elems(constructor, fqname, elems):
        """Make a function testing elems attribute value"""
        def method(self):
            """Test parser elems attribute value"""
            parser = constructor()
            self.assertEqual(parser.elems, elems)
        method.__doc__ = f'Test {fqname} elems attribute value'
        return method
    @staticmethod
    def make_test_accept(constructor, fqname, elems, accept):
        """Make a function testing parser accepts line"""
        @params(*accept)
        def method(self, line, expect):
            """Test parser accepts line"""
            parser = constructor()
            parsed = parser.parse(line)
            # test parsed value as a tuple
            self.assertEqual(expect, parsed)
            # test parsed value as a named tuple
            for (idx, name) in enumerate(elems):
                self.assertEqual(expect[idx], getattr(parsed, name))
        method.__doc__ = f'Test {fqname} accepts line'
        return method
    @staticmethod
    def make_test_reject(constructor, fqname, reject):
        """Make a function testing parser rejects line"""
        @params(*reject)
        def method(self, line):
            """Test parser rejects line"""
            parser = constructor()
            with self.assertRaises(ValueError):
                parser.parse(line)
        method.__doc__ = f'Test {fqname} rejects line'
        return method
    @staticmethod
    def make_test_discard(constructor, fqname, discard):
        """Make a function testing parser discards line"""
        @params(*discard)
        def method(self, line):
            """Test parser discards line"""
            parser = constructor()
            parsed = parser.parse(line)
            self.assertIsNone(parsed)
        method.__doc__ = f'Test {fqname} discards line'
        return method
