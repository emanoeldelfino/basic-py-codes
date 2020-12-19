import os
import pyperclip

print('Welcome to ℙƴ☂ℌøἤ Unicode writer\n')

strings = []

while True:
	try:
		string = input()
		strings.append(str(chr(int(string, 16))))
		os.system('clear')
		print(' '.join(strings))
	except KeyboardInterrupt:
		pyperclip.copy(''.join(strings))
		break

