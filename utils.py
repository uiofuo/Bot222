import requests
import json
from config import keys
class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'нвозможно перевести одинаковые валюты {base}.')

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionExeption(f'не удалось обработать валюту {quote}.')
    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionExeption(f'не удалось обработать валюту {base}.')
        
    try:
        amount = float(amount)
       except ValueError:
          raise ConvertionExeption(f'не удалось обработать количество {amount}')
          r = requests.get(f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={keys[quote]}&tsyms={keys[base]}')
          total_base = json.loads(r.content)[keys[base]]

          return total_base
