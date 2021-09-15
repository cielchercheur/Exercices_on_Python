# generate words with old keyphone

import sys


def print_words(number, cur, output, n):
    if cur == n:
        print(''.join(output), end=' ')
        return

    for _, letter in enumerate(buttons[number[cur]]):
        output.append(letter)
        print_words(number, cur + 1, output, n)
        output.pop()

        if number[cur] == 0 or number[cur] == 1:
            return


if __name__ == "__main__":
    buttons = dict([('2', ['a', 'b', 'c']),
                    ('3', ['d', 'e', 'f']),
                    ('4', ['g', 'h', 'i']),
                    ('5', ['j', 'k', 'l']),
                    ('6', ['m', 'n', 'o']),
                    ('7', ['p', 'q', 'r', 's']),
                    ('8', ['t', 'u', 'v']),
                    ('9', ['w', 'x', 'y', 'z'])])

    input_string = sys.stdin.readline().rstrip()
    length = len(input_string)
    print_words(input_string, 0, [], length)
    print()
