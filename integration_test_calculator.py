class TestCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_and_subtract(self):
        result = self.calc.add(5, 3)
        result = self.calc.subtract(result, 2)
        self.assertEqual(result, 6)
