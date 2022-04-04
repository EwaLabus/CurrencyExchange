from decimal import *
from api_connection import get_currency_exchange_values


def calculate_currency_amount(date, old_currency_symbol, new_currency_symbol, old_currency_amount):
    currency_dict= get_currency_exchange_values(date, old_currency_symbol, new_currency_symbol)
    new_currency_amount = round(Decimal(old_currency_amount) / Decimal(currency_dict[old_currency_symbol]) *
                                Decimal(currency_dict[new_currency_symbol]),2)

    return new_currency_amount
