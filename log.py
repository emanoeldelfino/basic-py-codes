import sys

while True:
    try:
        a = float(input('\nbase: '))
        b = float(input('logaritmando: '))
    except Exception as err:
        break

    if a == 1 and a != b:
        print('Invalid logarithm for base 1')
        sys.exit()
    elif a < 1 and a < b:
        op = 'minus'
    else:
        op = 'plus'

    v = a
    x = 0

    if op == 'plus':
        while v != b:
            x += 1
            v = a ** x
    else:
        while v != b:
            x -= 1
            v = a ** x

    print(f'\nlog {a} {b} = {x}, as {a} ** {x} = {b}')

