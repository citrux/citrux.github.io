import sys
import numpy as np
import time

PRIMES = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

def number(degrees):
    return np.prod(PRIMES[:len(degrees)] ** degrees)

def divisors(degrees):
    return np.prod(2*degrees+1)

# def to_string(degrees):
#     return ' • '.join(f'{p}^{d}' for p, d in zip(PRIMES, degrees) if d)

if __name__ == '__main__':
    s = int(sys.argv[1])
    t = time.time()
    # constructive initial guess
    # m is number of prime factors
    m = int(np.log(2 * s - 1) / np.log(3)) + 1
    result = np.array([1] * m)
    n = number(result)

    # let's get it
    ind = 0
    guess = np.array([0] * m)
    iters = 0
    while ind > -1:
        iters += 1
        guess[ind] += 1
        n_ = number(guess)

        if (ind and guess[ind] > guess[ind-1]) or n_ > n:
            # if state is unordered, make it ordered, setting value to 0 and move to previous degree
            # if current value is greater, than already found, also go to smaller numbers
            guess[ind] = 0
            ind -= 1
            continue

        if divisors(guess) + 1 > 2 * s:
            # looks good, if smaller than previous result, update it
            if n_ < n:
                result = guess.copy()
                n = n_
            # we don't need to make number bigger, because it already has at least s solutions
            guess[ind] = 0
            ind -= 1
        else:
            # not enough solutions, go to next factor
            if ind < m - 1:
                ind += 1

    print(f'Solution: {n}')
    print(f'It has {(divisors(result) + 1)//2} decompositions')
    print(f'Done in {iters} iters')
    print(time.time()-t)
