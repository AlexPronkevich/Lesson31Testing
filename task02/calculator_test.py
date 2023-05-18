import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    # arrang #подготовка
    # act     экшен
    # assert   утверждение

    def testAddPositive(self):
        a = 5
        b = 6
        expected = 11  # блок подготовки данных

        actual = Calculator.add(a, b)

        self.assertEqual(expected, actual)

    def testSubPositive(self):
        a = 5
        b = 6
        expected = -1  # блок подготовки данных

        actual = Calculator.sub(a, b)

        self.assertEqual(expected, actual)

    def testMulPositive(self):
        a = 5
        b = 6
        expected = 30  # блок подготовки данных

        actual = Calculator.mul(a, b)

        self.assertEqual(expected, actual)

    def testDivPositive(self):
        a = 10
        b = 2
        expected = 5  # блок подготовки данных

        actual = Calculator.div(a, b)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
