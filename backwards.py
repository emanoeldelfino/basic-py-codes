import sys


def backwards(*args, reverse_return=True):
    words = []
    for arg in args:
        words.append(arg[::-1])

    if reverse_return:
        words = reversed(words)
    return words


args = sys.argv[1:]

reversed_words = backwards(*args)

for word in reversed_words:
    print(word, end=' ')
print()
