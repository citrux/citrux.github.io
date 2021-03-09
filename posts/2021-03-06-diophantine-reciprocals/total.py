from math import prod, log
from itertools import product

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]


def number(degrees):
    return prod(p ** d for p, d in zip(PRIMES, degrees))


def divisors(degrees):
    return prod(2 * d + 1 for d in degrees)


def minimal(s):
    m = int(log(2*s)/log(3)) + 1
    n = prod(PRIMES[:m])

    ranges = [range(0, int(log(n) / log(PRIMES[i])) + 1) for i in range(m)]
    for degrees in product(*ranges):
        if divisors(degrees) > 2 * s - 1:
            n_ = number(degrees)
            if n_ < n:
                n = n_
    return n


if __name__ == '__main__':
    import sys
    s = int(sys.argv[1])
    print(minimal(s))
