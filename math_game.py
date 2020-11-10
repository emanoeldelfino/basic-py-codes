# jogo da matemática
from random import randint
from time import sleep


def operation(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == 'x':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        print('Error.')


def rank():
    print(f'\n{player1} ({player1_points}) x ({player2_points}) {player2}\n')


player1, player2 = [input(f'\nNickname of player {i}: ') for i in range(1, 3)]

play_again = True

while play_again:
    rounds = int(input('\nHow many rounds for each one? ')) * 2

    c = 1

    player = player2

    player1_points = player2_points = 0

    for c in range(0, rounds):
        print('\nRank: ')
        rank()
        if player == player2:
            player = player1
        else:
            player = player2

        while True:
            operator = input(f'\nWhich operator (+, -, x, /) {player}? ')
            if operator in ['+', '-', 'x', '/']:
                break
            else:
                print('Invalid operator. Try again.')

        num_range = 0
        while num_range not in range(5, 1001):
            num_range = int(input(f'\nChoose a number range between 5 and 1000 {player}: '))

        n1, n2 = [randint(1, num_range) for _ in range(2)]

        result = operation(n1, operator, n2)
        print(f'\n{n1} {operator} {n2} = ?')

        hint = input('\nDo you want a hint? [Y/N] ').upper()

        if hint and hint[0] == 'Y':
            num_hint = randint(1, result)

            if result > num_hint:
                print(f'Result is greater than {num_hint}.')
            else:
                print(f'Result is less or equal to {num_hint}.')

        user_answer = float(input(f'\nWhat is the result {player}? '))

        if user_answer == result:
            print(f'\nYou got that right {player}!')
            if player == player1:
                player1_points += 1
            else:
                player2_points += 1
        else:
            print(f'\nYou got that wrong {player}.')
            print(f'The correct answer was {result}.')

        sleep(3)

    print('\nFinal rank: ')
    rank()

    if player1_points > player2_points:
        print(f'{player1} has won the game!')
    elif player2_points > player1_points:
        print(f'{player2} ha won the game!')
    else:
        print("That's a draw!")

    sleep(2)

    play_again_ans = input('\nDo you want to play again? [Y/N] ').upper()
    if not play_again_ans or play_again_ans[0] != 'Y':
        play_again = False
