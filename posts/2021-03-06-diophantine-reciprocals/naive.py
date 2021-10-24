def solutions(n):
    return sum(n ** 2 % k == 0 for k in range(1, n + 1))


def minimal(s):
    n = 1
    while solutions(n) <= s:
        n += 1
    return n


if __name__ == '__main__':
    import sys

    s = int(sys.argv[1])
    print(minimal(s))
