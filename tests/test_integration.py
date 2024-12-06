import unittest
from main import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_add_and_subtract(self):
        calc = Calculator()
        result = calc.subtract(calc.add(5, 5), 3)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()