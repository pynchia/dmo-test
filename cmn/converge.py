"""
Play with the function
"""
import itertools as it

from cmn.function import c


def count_steps(m, n):
    return sum(
        1 for _ in it.takewhile(
            lambda v: v != 1,
            (c(m,k) for k in it.count(n))
        )
    ) + 1
