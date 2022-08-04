from unittest import TestCase, main
import doctest
import unittest
from learn_py import divisor


class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            divisor.divide(10, 0)


if __name__ == '__main__':
    main()
