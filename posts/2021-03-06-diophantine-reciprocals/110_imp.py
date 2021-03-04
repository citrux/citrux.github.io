from math import prod
import sys


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def number(degrees):
    return prod(p ** d for p, d in zip(PRIMES, degrees))

def divisors(degrees):
    return prod(2*d+1 for d in degrees)

def to_string(degrees):
    return ' • '.join(f'{p}^{d}' for p, d in zip(PRIMES, degrees) if d)

def leftmost_min(l):
    i = len(l) - 1
    while i > 0 and l[i-1] == l[i]:
        i -= 1
    return i

if __name__ == '__main__':
    s = int(sys.argv[1])

    # constructive initial guess
    result = []
    while not divisors(result) > 2*s-1:
        result.append(1)

    m = len(result)

    last = m-1
    iters = 0
    while last:
        if result[last] == 0 or (last < m-1 and result[last] == result[last+1]):
            last -=1
            continue

        guess = result[:]
        guess[last] -= 1
        if divisors(guess) > 2*s-1:
            result = guess[:]
            continue
        print(guess, last)
        greatest_prime_factor = PRIMES[last]
        stop = True
        for q in range(last, 0, -1):
            guess = result[:]
            guess[last] -= 1
            product = 1
            stop = True
            while greatest_prime_factor > product * PRIMES[0]:
                # find leftmost lowest value
                i = leftmost_min(guess[:q])
                # fill it or move left to find another
                while i >= 0:
                    iters += 1
                    if  product * PRIMES[i] < greatest_prime_factor and (i == 0 or guess[i-1] > guess[i]):
                        product *= PRIMES[i]
                        guess[i] += 1
                        break
                    i -= 1
                    print(i, q, last, guess)
                if divisors(guess) > 2*s-1:
                    result = guess[:]
                    stop = False
                    break
            # if not stop:
            #     break
        if stop:
            last -= 1

    n = number(result)
    print(f'Solution: {n} = {to_string(result)}')
    print(f'It has {(divisors(result) + 1)//2} decompositions')
    print(f'Done in {iters} iters')

    # incorrect for 115: 2310 = 2^1 • 3^1 • 5^1 • 7^1 • 11^1 but 1680 = 2^4 • 3^1 • 5^1 • 7^1
