#! python3
# money_GP_calc.py - Money Geometric Progression calculator.

# You may be amazed how numbers can get really big when Geometric Progression is# applied to them.

initial_value = float(input('\nInitial value: $'))
multiplication = int(input('Multiplication of the value: '))
days = int(input('Number of days: '))

values = [initial_value * multiplication ** day for day in range(days + 1)]

print()

for day, value in enumerate(values):
    print(f'day {day}: ${value}')

print(f'\nWith ${initial_value} being multiplied by {multiplication} each day by {days} days,'
      '\nat the end of this days this value would turn to be ${values[-1]}.')
