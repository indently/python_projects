import random


def roll_dice(amount: int = 2) -> list[int]:
    """
    Rolls some dice and returns the results as a list.

    :param amount: The amount of dice to roll.
    :return: A list of dice rolls.
    """
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')

            # To exit the game
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break

            # Try to parse the user_input to int
            print(*roll_dice(int(user_input)), sep=', ')
        except ValueError:
            print('(Please enter a valid number)')


if __name__ == '__main__':
    main()
