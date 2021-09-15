# Knuth–Morris–Pratt
# algorithm searches for occurrences of a "word" t within a main "text string" s
import sys


def kmp(long, short):
    j, k = 0, 0
    index = 0

    while j < len(long):
        if short[k] == long[k]:
            j += 1
            k += 1
            if k == len(short):
                return True
        else:
            k = index + 1
            j += 1
        index += 1

    return False


if __name__ == '__main__':
    s = list(sys.stdin.readline().rstrip())
    t = list(sys.stdin.readline().rstrip())
    if len(s) < len(t):
        print(False)
    elif len(s) == len(t):
        print(s == t)
    else:
        print(kmp(s, t))
