from timeit import Timer
import csv


def min_time(algorithm: str, n: int) -> float:
    timer = Timer(f's({n})', f'from {algorithm} import s')
    number, t = timer.autorange()
    repeat = 5 if t < 5 else 1
    raw_timings = timer.repeat(repeat, number)
    return min(dt / number for dt in raw_timings)


if __name__ == '__main__':
    import sys

    algorithm = sys.argv[1]

    csvfile = sys.stdout
    writer = csv.writer(csvfile)
    writer.writerow(['decompositions', 'time'])

    n = 1
    while True:
        t = min_time(algorithm, n)
        writer.writerow([n, f'{t:.1e}'])
        sys.stderr.write(f'{t}\n')

        if t > 30:
            break

        n *= 3
