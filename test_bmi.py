import unittest
from bminew2 import calculate_bmi, bmi_category


class TestBMI(unittest.TestCase):

    def test_bmi_math(self):
        bmi = calculate_bmi(175, 68)
        self.assertAlmostEqual(bmi, 26.60575259515571, places=6)

    def test_category_overweight(self):
        self.assertEqual(bmi_category(26.6), "Overweight")

    def test_category_boundaries(self):
        self.assertEqual(bmi_category(18.5), "Healthy")
        self.assertEqual(bmi_category(25), "Overweight")
        self.assertEqual(bmi_category(30), "Obesity")

    def test_height_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_bmi(150, 0)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            calculate_bmi("abc", 70)


if __name__ == "__main__":
    unittest.main()