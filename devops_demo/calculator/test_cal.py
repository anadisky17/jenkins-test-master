import unittest

from .cal import add


class Test(unittest.TestCase):
    def test_add_int(self):
        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_add_float(self):
        res = add(5.7, 9.6)
        self.assertEqual(15.3, res)

    def test_add_str(self):
        res = add('a', 'b')
        self.assertEqual(res, 'ab')

    def test_add_negative(self):
        res = add(-5, -6)
        self.assertEqual(res, -11)
