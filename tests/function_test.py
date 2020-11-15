import pytest

from cmn.function import c


def test_function(sample_mn_and_result):
    for mn, res in sample_mn_and_result:
        assert c(*mn) == res
