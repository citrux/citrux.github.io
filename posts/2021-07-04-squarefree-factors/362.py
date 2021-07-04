import sys
from functools import cache


PRIMES = []
SQUAREFREE = []
SQUAREFREE_FLAGS = []
F = {}


@cache
def count(n):
    res = n - 1
    for i in range(2, int(n ** 0.5) + 1):
        res += SQUAREFREE_FLAGS[i] * (n // (i * i))
    return res


def f(less_squarefree_index, upper_bound):
    stack = [(less_squarefree_index, upper_bound)]
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
    return f(0, n)


if __name__ == '__main__':
    n = int(sys.argv[1])
    l = int(n ** 0.5)
    primes_flags = [1] * (l + 3)
    SQUAREFREE_FLAGS = [-1] * (l + 3)
    for i in range(2, l + 3):
        if primes_flags[i]:
            PRIMES.append(i)
            for j in range(i + i, l + 3, i):
                primes_flags[j] = 0
        for p in PRIMES:
            if i * p > l + 2:
                break
            if i % p == 0:
                SQUAREFREE_FLAGS[i * p] = 0
                break
            SQUAREFREE_FLAGS[i * p] = -SQUAREFREE_FLAGS[i]
    SQUAREFREE = [i for i, f in enumerate(SQUAREFREE_FLAGS) if i > 1 and f]
    print(s(n))
