import itertools
import string
import time


def common_guess(word: str) -> str | None:
    """Checks a file filled with common words"""

    with open('words.text', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'


# Goes through every combination of chars
def brute_force(word: str, length: int, digits=False, symbols=False) -> str | None:
    """Performs brute force on finding a word"""

    # Modify this for total symbols
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'
        # print(guess, attempts) # Comment this out when you're not testing


def main():
    print('Searching...')
    password: str = 'pass1'

    # Get the start time
    start_time: float = time.perf_counter()

    # Search for common words before using the actual brute force
    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=5, digits=True, symbols=False):
            print(cracked)
        else:
            print('There was no match...')

    # Get the end time
    end_time: float = time.perf_counter()

    # Display the time it took
    print(round(end_time - start_time, 2), 's')


if __name__ == '__main__':
    main()
