import pytest

from cmn.function import c


def test_function(sample_mn_and_funct_results):
    for mn, res in sample_mn_and_funct_results:
        assert c(*mn) == res
