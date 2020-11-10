base = 2

for i in range(1, 10):
    num = base ** i
    print(f'{num:<3} -> {bin(num)}')
