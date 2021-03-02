from matplotlib import pyplot as plt
from math import log, prod
import numpy as np

from matplotlib import rc
rc('font',**{'family':'serif'})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage[utf8]{inputenc}\usepackage[T2A]{fontenc}\usepackage[russian]{babel}')
rc('axes', axisbelow=True)

minimal = __import__('110').minimal
number = __import__('110').number
divisors = __import__('110').divisors
PRIMES = __import__('110').PRIMES

# n(s)
# x = list(range(1, 301))
# y = [minimal(i) for i in x]
# y1, y2 = zip(*y)
# # plt.loglog(x, y2)
# # plt.show()
# plt.ylabel('Наименьшее $n$, для которого число разложений превышает $s$')
# plt.xlabel('Количество разложений $s$')
# plt.loglog(x, [number(ds) for ds in y1], 'k-', lw=1)
# plt.grid()
# plt.show()


# time 1
# x = np.array([1,3,10,30,100,200,300])
# y = np.array([5e-6, 3e-5, 3e-4, 7e-3, 7e-1, 4.33, 40])

# p = np.polyfit(np.log(x), np.log(y), 2)

# xl = np.linspace(0, np.log(1000), 100)
# yl = np.polyval(p, xl)

# xs = np.exp(xl)
# ys = np.exp(yl)

# plt.xlabel('Количество разложений')
# plt.ylabel('Время, с')
# plt.loglog(x, y, 'k+')
# plt.loglog(xs[xs<=max(x)], ys[xs<=max(x)], 'k-', lw=1)
# plt.loglog(xs[xs>max(x)], ys[xs>max(x)], 'k--', lw=1)
# plt.grid()
# plt.show()

# time 2
# x = np.array([1,3,10,30,100,300,1000])
# y = np.array([3e-6, 8e-6, 1e-4, 1e-3, 2e-2, .5, 9])

# p = np.polyfit(np.log(x), np.log(y), 2)

# xl = np.linspace(0, np.log(10000), 100)
# yl = np.polyval(p, xl)

# xs = np.exp(xl)
# ys = np.exp(yl)

# plt.xlabel('Количество разложений')
# plt.ylabel('Время, с')
# plt.loglog(x, y, 'k+')
# plt.loglog(xs[xs<=max(x)], ys[xs<=max(x)], 'k-', lw=1)
# plt.loglog(xs[xs>max(x)], ys[xs>max(x)], 'k--', lw=1)
# plt.grid()
# plt.show()

#time 3
x = np.array([1,       3,   10,   30,  100,  300, 1000,3000,10000,30000,100000,300000,1000000,3000000, 10000000])
y = np.array([4e-6, 1e-5, 3e-5, 7e-5, 2e-4, 5e-4, 1e-3,2e-3, 6e-3, 1e-2,  2e-2,  4e-2,   7e-2, 1e-1, 2e-1])

p = np.polyfit(np.log(x), np.log(y), 2)

xl = np.linspace(0, np.log(1e7), 100)
yl = np.polyval(p, xl)

xs = np.exp(xl)
ys = np.exp(yl)

plt.xlabel('Количество разложений')
plt.ylabel('Время, с')
plt.loglog(x, y, 'k+')
plt.loglog(xs[xs<=max(x)], ys[xs<=max(x)], 'k-', lw=1)
plt.loglog(xs[xs>max(x)], ys[xs>max(x)], 'k--', lw=1)
plt.grid()
plt.show()

# solutions

# @np.vectorize
# def solutions(n):
#     return sum(n**2 % k == 0 for k in range(1, n+1))

# plt.xlabel('$n$')
# plt.ylabel('Количество разложений $s(n)$')
# ns = np.arange(1, 100)
# plt.grid(axis='y')
# plt.bar(ns, solutions(ns), 1, color='lightblue', edgecolor='k')
# plt.show()