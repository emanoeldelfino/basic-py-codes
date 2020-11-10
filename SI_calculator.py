#! python3
# SI_calculator.py - Simple Interest Calculator.
principal = float(input('\nPrincipal Amount: $'))

while True:
    period_type = input('\nPeriod type, (D)ays, (M)onths or (Y)ears: ').upper()

    period_type = [value for value in ['Days', 'Months', 'Years'] if value[0] == period_type]

    if period_type:
        period_type = period_type[0]
        break
    else:
        print('Enter D for Days, M for Months and Y for Years.')

period_amount = int(input(f'Period of {period_type}: '))
rate = float(input('\nRate of Interest: '))

simple_interest = (principal * period_amount * rate) / 100

print(
    f'\nSimple Interest is ${simple_interest:.2f} for {period_amount} {period_type} with rate of interest of %{rate}.')

# # Portuguese simplified version
# capital = float(input('\nCapital: '))
# indice = float(input('Taxa (%): ')) / 100
# tempo = float(input('Meses: ')) / 12
# juros = capital * indice * tempo
# print('\nO valor dos juros é de R${:.2f}.'.format(j))
