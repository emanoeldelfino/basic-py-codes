from random import choice
import string
import sys
import subprocess


def random_values(array, length):
    return ''.join([choice(array) for _ in range(length)])


p1 = subprocess.Popen(['xclip', '-selection', 'clipboard', '-f'], stdin=subprocess.PIPE)

args = sys.argv[1:]

iters = int(args[0])

chars = string.ascii_lowercase

user = random_values(array=chars, length=iters) 

p1.communicate(input=(user.encode()))

