"""
Play with the function
"""
import itertools as it

from cmn.function import c


def count_steps(m, n):
    """
    Counts the steps it takes cm(n) to reach 1
    letting n grow
    """
    return sum(
        1 for _ in it.takewhile(
            lambda v: v != 1,
            (c(m,k) for k in it.count(n))
        )
    ) + 1


def count_steps_for_many_m(stop, start=1):
    """
    Yields the steps it takes cm(n) to reach 1
    letting n grow
    for any m in the range [start, stop]
    """
    for m in range(start, stop+1):
        yield count_steps(m, 1)
