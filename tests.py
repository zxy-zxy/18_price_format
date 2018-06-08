import unittest

from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_thousand_integer_number(self):
        self.assertEqual('5 340', format_price(5340))

    def test_ten_thousand_integer_number(self):
        self.assertEqual('10 450', format_price(10450))

    def test_ten_thousand_float_number(self):
        self.assertEqual('10 450.50', format_price(10450.5))

    def test_float_number_with_long_decimal_part(self):
        self.assertEqual('125 500', format_price(125500.001))

    def test_float_number_with_long_decimal_part_correct_rounding(self):
        self.assertEqual('125 501', format_price(125500.996))

    def test_negative_number(self):
        self.assertEqual('-10 350', format_price(-10350))

    def test_string_input_equals_to_none(self):
        self.assertIsNone(None, format_price('string_input'))

    def test_list_equals_to_none(self):
        self.assertIsNone(None, format_price([1, 2, 3]))

    def test_tuple_equals_to_none(self):
        self.assertIsNone(None, format_price((1231, 'AADDBB')))

    def test_dict_equals_to_none(self):
        self.assertIsNone(None, format_price({'key': 'value'}))
