import pytest

from cmn.converge import count_steps

def test_convergence_to_1(sample_mn_and_converge_to_1_steps):
    for mn, steps in sample_mn_and_converge_to_1_steps:
        assert count_steps(*mn) == steps
