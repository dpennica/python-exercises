import unittest
from sequence.fibonacci import fib


class TestFibonacci(unittest.TestCase):

    def test_fib_0(self):
        result = []
        self.assertEqual(result, fib(0))

    def test_fib_1(self):
        result = [0]
        self.assertEqual(result, fib(1))

    def test_fib_2(self):
        result = [0, 1, 1]
        self.assertEqual(result, fib(2))

    def test_fib_10(self):
        result = [0, 1, 1, 2, 3, 5, 8]
        self.assertEqual(result, fib(10))

    def test_fib_20(self):
        result = [0, 1, 1, 2, 3, 5, 8, 13]
        self.assertEqual(result, fib(20))
