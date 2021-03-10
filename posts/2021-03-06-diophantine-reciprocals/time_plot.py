import argparse
import numpy as np

from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib import rc

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', type=str, default='png')
parser.add_argument('filename')
args = parser.parse_args()

rc('figure', figsize=(10, 8))

if args.format == 'svg':
    rc('svg', fonttype='none')
    rc('savefig', transparent=True)
else:
    rc('font', family='serif')
    rc('text', usetex=True)
    rc('text.latex', preamble=r'\usepackage[utf8]{inputenc}\usepackage[T2A]{fontenc}\usepackage[russian]{babel}')
    rc('axes', axisbelow=True)

x, y = np.loadtxt(args.filename, skiprows=1, delimiter=',', unpack=True)

p = np.polyfit(np.log(x), np.log(y), 2)

xl = np.linspace(0, np.log(2*max(500, *x)), 100)
yl = np.polyval(p, xl)

xs = np.exp(xl)
ys = np.exp(yl)

plt.xlabel('Количество разложений')
plt.ylabel('Время, с')
plt.loglog(x, y, 'k+')
plt.loglog(xs, ys, 'k-', lw=1)
plt.grid()

filepath = Path(args.filename)
outname = filepath.parent / (filepath.stem + '.' + args.format)
plt.savefig(outname)

if args.format == 'svg':
    import re

    with open(outname, 'r') as f:
        data = f.read()
    data = re.sub('#000000', 'currentColor', data)
    data = re.sub(r'font-(family|style|weight):[^;]+;', '', data)
    with open(outname, 'w') as f:
        f.write(data)

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