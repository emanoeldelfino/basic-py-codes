import signal

def timeout(signum, frame):
	raise Exception('Your time is over!')

signal.signal(signal.SIGALRM, timeout)

try:
	signal.alarm(5)
	name = input('What is yourname? ')
	signal.alarm(0)
except Exception as e:
	name = 'Unknown'

print('Welcome', name, '!')

