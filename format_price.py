import argparse
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'price',
        help='Price to format.'
    )

    return parser


def format_price(price):
    try:
        float(price)
    except (TypeError, ValueError):
        return None

    try:
        price_in_decimal_format = Decimal(price).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_EVEN
        )
    except InvalidOperation:
        return None

    if int(price_in_decimal_format) == price_in_decimal_format:
        format_specs = ',.0f'
    else:
        format_specs = ',.2f'

    formatted_price = format(
        price_in_decimal_format,
        format_specs
    ).replace(',', ' ')

    return formatted_price


if __name__ == '__main__':
    args_parser = create_parser()
    args = args_parser.parse_args()

    formatted_price = format_price(args.price)
    if formatted_price is None:
        sys.exit('Invalid input.')

    print(formatted_price)
