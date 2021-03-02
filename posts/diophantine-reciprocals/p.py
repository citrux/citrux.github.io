PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
divisors = 1
n = 1
m = 0
for p in PRIMES:
    m += 1
    n *= p
    divisors *= 3
    if divisors > 1999:
        break
print(n, m)
