import unittest

from main import number_to_string


class Test(unittest.TestCase):

    def test_casual_case_1_func(self):
        self.assertEqual(number_to_string(1234567890).strip().lower(),
                         'один миллиард двести тридцать четыре миллиона пятьсот шестьдесят семь тысяч восемьсот '
                         'девяносто'.strip().lower())

    def test_casual_case_2_func(self):
        self.assertEqual(number_to_string(22234124412).strip().lower(),
                         'Двадцать два миллиарда двести тридцать четыре миллиона сто двадцать четыре тысячи четыреста '
                         'двенадцать'.strip().lower())
