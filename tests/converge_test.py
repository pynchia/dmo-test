import pytest

from cmn.converge import count_steps, count_steps_for_many_m

def test_convergence_to_1(sample_mn_and_converge_to_1_steps):
    for mn, steps in sample_mn_and_converge_to_1_steps:
        assert count_steps(*mn) == steps

def test_steps_4_m(steps_4_m_values):
    for steps, expected_steps in zip(
                                    count_steps_for_many_m(len(steps_4_m_values)),
                                    steps_4_m_values):
        assert steps == expected_steps
