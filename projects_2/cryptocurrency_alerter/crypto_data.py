import requests
from dataclasses import dataclass
from typing import Final

BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        return f'{self.name} ({self.symbol}): €{self.current_price:,}'


def get_coins() -> list[Coin]:
    """
    Gets coins from an api and returns them as a list[Coin]
    API: https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur

    """

    # Make the request in euros
    payload = {'vs_currency': 'eur', 'order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    json: dict = data.json()

    # Create coins and add them to a coin list
    coins_list: list[Coin] = []
    for item in json:
        current_coin: Coin = Coin(name=item.get('name'),
                                  symbol=item.get('symbol'),
                                  current_price=item.get('current_price'),
                                  high_24h=item.get('high_24h'),
                                  low_24h=item.get('low_24h'),
                                  price_change_24h=item.get('price_change_24h'),
                                  price_change_percentage_24h=item.get('price_change_percentage_24h'))
        coins_list.append(current_coin)

    return coins_list
