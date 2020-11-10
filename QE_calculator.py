#! python3
# QE_calculator.py - Quadratic Equation Calculator.

print('-' * 30)
print('Quadratic Equation Calculator')
print('-' * 30)

a, b, c = [float(input(f'\n{letter} value: ')) for letter in 'ABC']
delta = b ** 2 - 4 * a * c

x = [(-b), (delta ** 0.5), 2 * a]
x1 = (x[0] + x[1]) / x[2]
x2 = (x[0] - x[1]) / x[2]

print()

print(f'Δ  = {delta:>5.0f}')
print(f'x1 = {x1:>5.2f}')
print(f'x2 = {x2:>5.2f}')

# print('\nΔ = {:.0f}.\nx1 = {:.2f}.\nx2 = {:.2f}.'.format(delta, x1, x2))
