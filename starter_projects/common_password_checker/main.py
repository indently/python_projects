def check_password(password: str):
    """
    Checks whether a password is in the 100.000 most common passwords.
    Sourced from: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt

    """

    # Open up the file with most common passwords
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    # If any of the words are equal to the password, return True
    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: ❌ (#{i})')
            return  # Exit the function as soon as we have a match

    # If the password is not located in the common passwords, it's unique
    print(f'{password}: ✅ (Unique)')


def main():
    # Check password
    user_password: str = input('Enter a password: ')
    check_password(password=user_password)


if __name__ == '__main__':
    main()
