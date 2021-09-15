# for matrix NxM (of INT types) find up/down/left/right neighbours elements

import sys

def sortedprint(listed):
    # print sorted values of neighbours
    print(*sorted(listed))


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    if n <= 1 and m <= 1:
        print()
        sys.exit(0)
    matrix = []
    for i in range(n):
        row = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
        matrix.append(row)
    i = int(sys.stdin.readline().rstrip())
    j = int(sys.stdin.readline().rstrip())
    # vectors
    if n == 1: # 1 line
        if j == 0:
            print(matrix[0][1])
        elif j == m-1:
            print(matrix[0][m-2])
        else:
            sortedprint([matrix[0][j-1], matrix[0][j+1]])
        sys.exit(0)
    if m == 1: # 1 row
        if i == 0:
            print(matrix[1][0])
        elif i == n-1:
            print(matrix[n-2][0])
        else:
            sortedprint([matrix[i-1][0], matrix[i+1][0]])
        sys.exit(0)
    # normal matrix
    # corners
    if i == 0 and j == 0:
        sortedprint([matrix[0][1], matrix[1][0]])
    elif i == 0 and j == m-1:
        sortedprint([matrix[0][m-2], matrix[1][m-1]])
    elif i == n-1 and j == 0:
        sortedprint([matrix[n-2][0], matrix[n-1][1]])
    elif i == n-1 and j == m-1:
        sortedprint([matrix[n-1][m-2], matrix[n-2][m-1]])
    # borders
    elif i == 0:
        sortedprint([matrix[0][j-1], matrix[0][j+1], matrix[1][j]])
    elif j == 0:
        sortedprint([matrix[i-1][0], matrix[i+1][0], matrix[i][1]])
    elif i == n-1:
        sortedprint([matrix[n-1][j-1], matrix[n-1][j+1], matrix[n-2][j]])
    elif j == m-1:
        sortedprint([matrix[i][m-2], matrix[i-1][m-1], matrix[i+1][m-1]])
    # middle part
    else:
        sortedprint([matrix[i-1][j], matrix[i][j-1], matrix[i+1][j], matrix[i][j+1]])
