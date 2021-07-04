import sys

SQUAREFREE = []


def sieve(n):
    flags = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if not flags[i]:
            continue
        for j in range(2 * i, n + 1, i):
            flags[j] = False

    return [i for i, is_prime in enumerate(flags) if is_prime]


def squarefree_sieve(n):
    flags = [False, False] + [True] * (n - 1)
    primes = sieve(n)
    for i in range(2, n + 1):
        for p in primes:
            if i * p > n:
                break
            if i % p == 0:
                flags[i * p] = False
                break
            flags[i * p] = flags[i]

    return [i for i, is_prime in enumerate(flags) if is_prime]


def f(i, n):
    if i >= len(SQUAREFREE) or SQUAREFREE[i] > n:
        return 0
    return 1 + f(i, n // SQUAREFREE[i]) + f(i + 1, n)


def s(n):
    SQUAREFREE[:] = squarefree_sieve(n)
    return f(0, n)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(s(n))
