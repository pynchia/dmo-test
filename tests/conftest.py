import pytest


@pytest.fixture
def mn_values(scope='session'):
    return [
        (1, 1),
        (2, 1),
        (1, 2),
        (1, 3),
        (2, 2),
        (3, 3),
    ]

@pytest.fixture
def sample_mn_and_funct_results(mn_values):
    EXPECTED_RESULTS = [
        1,
        2,
        4,
        2,
        1,
        5,
    ]
    return zip(mn_values, EXPECTED_RESULTS)

@pytest.fixture
def sample_mn_and_converge_to_1_steps(mn_values):
    STEPS = [
        1,
        2,
        3,
        2,
        1,
        6,
    ]
    return zip(mn_values, STEPS)
