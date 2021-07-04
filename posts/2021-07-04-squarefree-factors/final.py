import sys
from functools import cache


SQUAREFREE = []
SQUAREFREE_SIGNS = []
F = {}


def sieve(n):
    flags = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if not flags[i]:
            continue
        for j in range(2 * i, n + 1, i):
            flags[j] = False

    return [i for i, is_prime in enumerate(flags) if is_prime]


def squarefree_signs(n):
    s = [0, 0] + [-1] * (n - 1)
    primes = sieve(n)
    for i in range(2, n + 1):
        for p in primes:
            if i * p > n:
                break
            if i % p == 0:
                s[i * p] = 0
                break
            s[i * p] = -s[i]
    return s


@cache
def count(n):
    result = n - 1
    for i, sign in enumerate(SQUAREFREE_SIGNS):
        if i < 2:
            continue
        if i * i > n:
            break
        result += sign * (n // (i * i))
    return result


def f(i, n):
    stack = [(i, n)]
    while stack:
        i, n = stack[-1]
        if (i, n) in F:
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
    SQUAREFREE_SIGNS[:] = squarefree_signs(int(n ** 0.5) + 1)
    SQUAREFREE[:] = [i for i, s in enumerate(SQUAREFREE_SIGNS) if s]

    return f(0, n)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(s(n))
