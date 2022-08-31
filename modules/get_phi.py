#! /usr/local/bin/python

import sys
import math
sys.path.insert(1, '..')

from utils.mathutils import PHI, SQRT_5

def lucas(nth: int, a: int, b: int):
    for i in range(1, nth + 1):
        result = a
        [a, b] = [b, a + b]
    return result


def fib(nth: int):
    [a, b] = [1, 1]
    for i in range(1, nth + 1):
        result = a
        [a, b] = [b, a+b]
    return result


def get_phi(max: int):
    rows = []
    for i in range(1, max+1):
        [f, l] = [fib(i), lucas(i, 1, 3)]
        phi = "(%d V5 + %d) / 2" % (f, l)
        real = (f * SQRT_5 + l) / 2
        fib_approx = real / SQRT_5
        fib_exact = round(fib_approx)
        diff = fib_exact - fib_approx
        row = { "nth": i, "fraction": phi, "real": real, "fib_approx": fib_approx, "fib_exact": fib_exact, "diff": diff, "[F, F*SQRT_5, L, L/SQRT_5]": [f, f * SQRT_5, l, l/SQRT_5] }
        rows.append(row)
    return rows

