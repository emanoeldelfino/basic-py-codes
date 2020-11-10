#! python3
# guess_the_number.py - An interactive guess the number game.

from random import randint

num_range = 0
while num_range not in range(2, 101):
    num_range = int(input('\nMax range of the number (2-100): '))
    if num_range not in range(2, 101):
        print('Only range between 2 and 100 is accepted.')

answer = randint(1, num_range)

if num_range == 2:
    guesses = 1
else:
    while True:
        guesses = int(input(f'\nNumber of guesses (1-{num_range - 1}): '))
        if guesses in range(1, num_range):
            break
        else:
            print(f'Number of guesses should be between 1 and {num_range - 1}.')

while guesses:
    while True:
        guess = int(input(f'\nEnter a number between 1-{num_range}: '))
        if guess in range(1, num_range + 1):
            break
        else:
            print(f'Guess should be between 1-{num_range}.')

    if guess == answer:
        print('\nYou have won, congratulations!')
        break
    else:
        guesses -= 1

if not guesses:
    print(f'\nYou have run out of guesses, the answer was {answer}.')
