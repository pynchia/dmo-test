import pytest

import cmn
from cmn.cli import cli


@pytest.fixture
def sample_mn_and_result():
    MN_VALUES = [
        (1, 1),
        (2, 1),
        (1, 2),
        (1, 3),
        (2, 2),
        (3, 3),
    ]
    EXPECTED_RESULTS = [
        1,
        2,
        4,
        2,
        1,
        5,
    ]
    return zip(MN_VALUES, EXPECTED_RESULTS)
