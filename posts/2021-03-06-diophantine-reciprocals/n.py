import argparse
import numpy as np

from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib import rc

from improved import minimal, number

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


x = list(range(1, 301))
y = [minimal(i) for i in x]
y1, y2 = zip(*y)
# plt.loglog(x, y2)
# plt.show()
plt.ylabel('Наименьшее $n$, для которого число разложений превышает $s$')
plt.xlabel('Количество разложений $s$')
plt.loglog(x, [number(ds) for ds in y1], 'k-', lw=1)
plt.grid()

outname = f'least_numbers.{args.format}'
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