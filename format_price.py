import argparse
import sys
from decimal import Decimal, InvalidOperation


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'number',
        help='Number to format'
    )

    return parser


def format_price(price):
    try:
        price_in_decimal_format = Decimal(price)
    except InvalidOperation:
        raise ValueError

    if price_in_decimal_format <= 0:
        raise ValueError

    return str.replace(
        '{:,.2f}'.format(price_in_decimal_format),
        ',',
        ' '
    )


if __name__ == '__main__':
    args_parser = create_parser()
    args = args_parser.parse_args()

    try:
        formatted_price = format_price(args.number)
    except ValueError:
        sys.exit('Invalid input.')

    print(formatted_price)
