def get_money(msg=''):
    while True:
        try:
            value = float(input(msg))
            if value < 0:
                raise ValueError
        except ValueError:
            print('Invalid value. Only floats greater or equal 0 are allowed.')
        else:
            return value


income = get_money('\nYour income: $')

expenses = []

while True:
    expense = get_money('\nEnter an expense (0 for stopping): $')

    if expense:
        expenses.append(expense)
    else:
        break

remaining_income = income - sum(expenses)

print(f'\nYour remaining income is ${remaining_income:.2f}.')

if sum(expenses) > income * 9 / 10:
    print("\nYou're spending too much, you should try to reduce your expenses!")
