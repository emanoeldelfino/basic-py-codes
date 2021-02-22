#! python3

import sys
import string
import secrets

chars = string.printable[:-6]

class InvalidLength(Exception):
	pass


class InvalidCommand(Exception):
	pass


print()

try:
	if len(sys.argv) == 1:
		length = 10
	elif len(sys.argv) == 2:
		length = int(sys.argv[1])

		if length < 10 or length > 25:
			raise InvalidLength()
	else:
		raise InvalidCommand()	
except InvalidCommand:
	print('Invalid Command.')
	print(f'Usage: python {__file__} <length>')
except InvalidLength:
	print('Password length must be between 10 and 25 characters.')
except Exception as err:
	print('Error: ')
	print(err)
else:
	password = ''.join(secrets.choice(chars) for _ in range(length))

	print('Password: ')
	print(password)

print()

