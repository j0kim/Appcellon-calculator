import unittest
import calc

class testCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-2, 3), 1)
        self.assertEqual(calc.add(2, -3), -1)
        self.assertGreater(calc.add(2,3), 4)
        self.assertLessEqual(calc.add(2,-3), 0)
        self.assertNotEqual(calc.add(2,3), 6)
        self.assertIsInstance(calc.add(5, 4), int)
        self.assertIsInstance(calc.add(5, 2.4), float)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.subtract(-2, 3), -5)
        self.assertEqual(calc.subtract(2, -3), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-2, 3), -6)
        self.assertEqual(calc.multiply(2, -3), -6)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(12, 3), 4)
        self.assertEqual(calc.divide(3, 2), 1.5)

        with self.assertRaises(ValueError):
            calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()