import sys
import math


if __name__ == '__main__':
    #  integer factorization is the decomposition of a composite number
    #  into a product of smaller integers.
    #  If these factors are further restricted to prime numbers,
    #  the process is called prime factorization.
    a = int(sys.stdin.readline().rstrip())
    fact = []
    i = 2
    while i <= math.sqrt(a):
        if a % i == 0:
            fact.append(i)
            a //= i
        else:
            i += 1
    fact.append(a)
    print(*fact)
