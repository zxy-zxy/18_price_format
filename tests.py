import unittest

from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_thousand_integer_number(self):
        self.assertTrue('5 340', format_price(5340))

    def test_ten_thousand_integer_number(self):
        self.assertTrue('10 450', format_price(10450))

    def test_ten_thousand_float_number(self):
        self.assertTrue('10 450.50', format_price(10450.5))

    def test_float_number_with_long_decimal_part(self):
        self.assertTrue('125 500', format_price(125500.001))

    def test_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            format_price(-12500)

    def test_string_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            format_price('string input')
