import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (False, False, False),
    (True, False, True),
    (False, True, True),
    (True, True, False),
]


@pytest.mark.parametrize('v1, v2, expected', testdata)
def test_run(v1, v2, expected):
    assert main.run(v1, v2) == expected
