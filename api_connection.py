import requests

api_adress = 'http://api.exchangeratesapi.io/v1/'
api_key = 'access_key=d2121c47af8d0888f0e66456816b1624'


def get_currency_exchange_values(date, old_currency_symbol, new_currency_symbol):
    currency_rate = {old_currency_symbol: 0.0, new_currency_symbol: 0.0}
    url = api_adress + date + '?' + api_key + '&symbols=' + old_currency_symbol + ',' + new_currency_symbol
    page_content_dict = requests.get(url).json()
    if 'success' in page_content_dict:
        if page_content_dict['success'] == True:
            currency_rate = page_content_dict['rates']

    return currency_rate


def get_all_currencies_labels():
    url = api_adress + 'symbols?' + api_key
    page_content_dict = requests.get(url).json()
    labels = []
    for key in page_content_dict['symbols'].keys():
        labels.append(str(key))

    return labels
