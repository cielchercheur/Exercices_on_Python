import sys


def generate(cur, open, close, n):
    if len(cur) == 2 * n:
        print(cur)
    if open < n:
        generate(cur + '(', open + 1, close, n)
    if close < open:
        generate(cur + ')', open, close + 1, n)


if __name__ == "__main__":
    # with Catalan numbers
    n = int(sys.stdin.readline().rstrip())
    generate('', 0, 0, n)
