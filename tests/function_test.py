import pytest

from cmn.function import c, SeqValueError


def test_function(sample_mn_and_funct_results):
    for mn, res in sample_mn_and_funct_results:
        assert c(*mn) == res

def test_fail_low_m():
    with pytest.raises(SeqValueError):
        c(-1, 3)
