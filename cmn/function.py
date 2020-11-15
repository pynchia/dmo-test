"""
The math function
"""
import itertools as it
import logging


log = logging.getLogger()


class SeqValueError(Exception):
    pass


def memoize(f):
    """
    A very basic caching mechanism
    """
    cache = {}
    def cached_f(*mn):
        if mn not in cache:
            cache[mn] = f(*mn)
            log.info(f"cache miss with {mn}")
        else:
            log.info(f"cache hit with {mn}")
        return cache[mn]
    return cached_f

@memoize
def c(m,n):
    log.info(f"enter c({m=}, {n=})")
    if n<=1:
        log.info(f"bottom of recursion: returning {m}")
        return m
    if m<0:
        raise SeqValueError("m must be greater or equal than 0")
    cmn1 = c(m, n-1)
    if cmn1 % 2 == 0: # even
        ret_val = cmn1 // 2  # to preserve integers, otherwise we get floats as well
    else:
        ret_val = cmn1 * 3 + 1
    log.info(f"returning {ret_val}")
    return int(ret_val)
