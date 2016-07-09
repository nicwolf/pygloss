"""Test functions for translate module

"""
import unittest

import pygloss
from pygloss import translate


class TestTranslateMethods(unittest.TestCase):

    def test_integer_string_translate(self):
        # A couple of correct use cases
        self.assertEqual(translate.translate_integer_string('12', '0123456789', '01'), '1100')
        self.assertEqual(translate.translate_integer_string('Foo', 'oF8', '0123456789'), '9')
        # The function should fail if anything other than a string is passed
        # in.
        with self.assertRaises(TypeError):
            translate.translate_integer_string(['b'], 'bbb', 'aaa')
        with self.assertRaises(TypeError):
            translate.translate_integer_string(1, '0123456789', '01')
        with self.assertRaises(TypeError):
            translate.translate_integer_string([0], [1], [22])
