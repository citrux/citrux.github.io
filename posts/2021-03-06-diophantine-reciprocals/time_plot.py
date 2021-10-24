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
rc('axes', axisbelow=True)

if args.format == 'svg':
    rc('svg', fonttype='none')
    rc('savefig', transparent=True)
else:
    rc('font', family='serif')
    rc('text', usetex=True)
    rc('text.latex', preamble=r'\usepackage[utf8]{inputenc}\usepackage[T2A]{fontenc}\usepackage[russian]{babel}')

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
