import argparse
import numpy as np

from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib import rc

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', type=str, default='png')
args = parser.parse_args()

rc('figure', figsize=(10, 8))
rc('axes', axisbelow=True)

if args.format == 'svg':
    rc('svg', fonttype='none')
    rc('savefig', transparent=True)
else:
    rc('font', family='serif')
    rc('text', usetex=True)
    rc('text.latex', preamble=r'\usepackage[utf8]{inputenc}\usepackage[T2A]{fontenc}\usepackage[russian]{babel}')


@np.vectorize
def solutions(n):
    return sum(n**2 % k == 0 for k in range(1, n+1))

plt.xlabel('$n$')
plt.ylabel('Количество разложений $s(n)$')
ns = np.arange(1, 101)
plt.grid(axis='y')
plt.bar(ns, solutions(ns), 1, color='lightblue', edgecolor='gray', alpha=.8)

outname = f'solutions.{args.format}'
plt.savefig(outname)

if args.format == 'svg':
    import re

    with open(outname, 'r') as f:
        data = f.read()

    # remove height and width attributes for responsiveness
    data = re.sub(r'(<svg [^>]*)height="[^"]+"', r'\1', data)
    data = re.sub(r'(<svg [^>]*)width="[^"]+"', r'\1', data)

    # use default font
    data = re.sub(r'font-(family|style|weight):[^;]+;', '', data)

    # dark-mode support:
    # set font color to currentColor
    data = re.sub(r'(</style>)', r' text,tspan{fill:currentColor}\1', data)
    # set black stroke to currentColor
    data = re.sub('#000000', 'currentColor', data)

    with open(outname, 'w') as f:
        f.write(data)
