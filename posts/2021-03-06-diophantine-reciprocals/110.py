import sys

from math import prod

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def number(degrees):
    return prod(p ** d for p, d in zip(PRIMES, degrees))


def divisors(degrees):
    return prod(2 * d + 1 for d in degrees)


def to_string(degrees):
    return ' • '.join(f'{p}^{d}' for p, d in zip(PRIMES, degrees) if d)


def minimal(s):
    # constructive initial guess
    result = []
    while divisors(result) <= 2 * s - 1:
        result.append(1)
    n = number(result)
    m = len(result)

    # let's get it
    i = 0
    guess = [0] * m
    iters = 0
    while i > -1:
        iters += 1
        guess[i] += 1
        n_ = number(guess)

        if (i and guess[i] > guess[i - 1]) or n_ > n:
            # if state is unordered, make it ordered, setting value to 0 and move to previous degree
            # if current value is greater, than already found, also go to smaller numbers
            guess[i] = 0
            i -= 1
            continue

        if divisors(guess) + 1 > 2 * s:
            # looks good, if smaller than previous result, update it
            if n_ < n:
                result = guess[:]
                n = n_
            # we don't need to make number bigger, because it already has at least s solutions
            guess[i] = 0
            i -= 1
        else:
            # not enough solutions, go to next factor
            if i < m - 1:
                i += 1
    return result, iters


if __name__ == '__main__':
    s = int(sys.argv[1])

    result, iters = minimal(s)
    n = number(result)

    print(f'Solution: {n} = {to_string(result)}')
    print(f'It has {(divisors(result) + 1)//2} decompositions')
    print(f'Done in {iters} iters')
