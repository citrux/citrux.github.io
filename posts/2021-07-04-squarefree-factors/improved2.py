import sys
from functools import cache

SQUAREFREE = []
PRIMES = []
F = {}


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


def g(i, n):
    if PRIMES[i] * PRIMES[i] > n:
        return 0

    k = n // (PRIMES[i] * PRIMES[i])
    return k - sum(g(j, k) for j in range(i))


@cache
def count(n):
    nonsquarefree_count = 1
    for i, p in enumerate(PRIMES):
        if p * p > n:
            break
        nonsquarefree_count += g(i, n)
    return n - nonsquarefree_count


def f(i, n):
    stack = [(i, n)]
    while stack:
        i, n = stack[-1]
        if (i, n) in F:
            stack.pop()
            continue

        if i >= len(SQUAREFREE) or SQUAREFREE[i] > n:
            F[(i, n)] = 0
            stack.pop()
            continue

        if SQUAREFREE[i] * SQUAREFREE[i] > n:
            F[(i, n)] = count(n) - i
            stack.pop()
            continue

        x = F.get((i, n // SQUAREFREE[i]))
        y = F.get((i + 1, n))

        if x is None:
            stack.append((i, n // SQUAREFREE[i]))
            continue
        if y is None:
            stack.append((i + 1, n))
            continue
        F[(i, n)] = 1 + x + y
    return F[(i, n)]


def s(n):
    F.clear()
    PRIMES[:] = sieve(int(n ** 0.5) + 1)
    SQUAREFREE[:] = squarefree_sieve(int(n ** 0.5) + 4)
    return f(0, n)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(s(n))
