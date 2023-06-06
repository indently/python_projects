from crypto_data import get_coins, Coin


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    """Creates an alert for the given price range of a coin"""

    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                # Add the code you want to be executed if a coin reaches
                print(coin, '!!!TRIGGER!!!')
            else:
                print(coin)


if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    # Create a loop for these to create live alerts
    alert('btc', bottom=10, top=20_000, coins_list=coins)
    alert('eth', bottom=1800, top=1900, coins_list=coins)
    alert('xrp', bottom=0.47, top=0.48, coins_list=coins)
