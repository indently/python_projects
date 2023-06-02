import string
import secrets


def contains_upper(password: str) -> bool:
    """Checks whether a password contains uppercase characters"""

    for char in password:
        if char.isupper():
            return True

    return False  # There were no uppercase chars


def contains_symbols(password: str) -> bool:
    """Checks whether a password contains symbols"""

    for char in password:
        if char in string.punctuation:
            return True

    return False  # There were no uppercase chars


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    """
    Generates a password based on the users specifications

    :param length: The length of the password
    :param symbols: Password should include symbols
    :param uppercase: Password should include uppercase letters
    :return: str
    """

    # Create a combination of characters to choose from
    combination: str = string.ascii_lowercase + string.digits

    # If the user wants symbols, add punctuation to the combination
    if symbols:
        combination += string.punctuation

    # If the user wants uppercase, add uppercase to the combination
    if uppercase:
        combination += string.ascii_uppercase

    # Get the length of the combination characters
    combination_length: int = len(combination)

    # Create a new password variable
    new_password: str = ''

    # Append to the new_password a new random character for each iteration
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


if __name__ == '__main__':
    # Generate 5 random passwords
    for i in range(1, 6):
        new_pass: str = generate_password(length=15, symbols=True, uppercase=True)
        specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'

        print(f'{i} -> {new_pass} ({specs})')
