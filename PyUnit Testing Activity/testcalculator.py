import unittest
from calculator import  Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3, 2), 5)
        self.assertEqual(Calculator.add(99, 1), 100)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 2), 1)
        self.assertEqual(Calculator.subtract(65, 30), 35)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 2), 6)
        self.assertEqual(Calculator.multiply(10, 9), 90)

    def test_divide(self):
        self.assertEqual(Calculator.divide(3, 3), 1)
        self.assertEqual(Calculator.divide(5, 10), 0.5)


if __name__ == "__main__":
    unittest.main()