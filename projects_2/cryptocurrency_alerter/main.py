from crypto_data import get_coins, Coin


def check_crypto(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
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
    check_crypto('btc', bottom=10, top=20_000, coins_list=coins)
    check_crypto('eth', bottom=10, top=1_700, coins_list=coins)
    check_crypto('xrp', bottom=0.47, top=0.48, coins_list=coins)
