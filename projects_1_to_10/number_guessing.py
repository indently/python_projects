from random import randint

# Start the program with basic setup
lower_num, upper_num = 1, 10
random_number: int = randint(lower_num, upper_num)
print(f'Guess the number in the range from {lower_num} to {upper_num}.')

# Run an infinite loop for the game
while True:
    # Get the user guess
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    # Check the user guess
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('You guessed it!')
        break
