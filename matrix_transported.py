# basic matrix transposition

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    matrix = []
    for i in range(n):
        matrix.append([x for x in sys.stdin.readline().rstrip().split(' ')])
    transposed = [ [matrix[y][x] for y in range(n)] for x in range(m) ]
    for i in range(m):
        print(*transposed[i])
