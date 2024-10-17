import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('rock', 'PAPER', 2),
    ('scissors', 'paper', 1),
    ('rock', 'paper', 2),
    ('SCISSORS', 'Rock', 2),
    ('paper', 'scissors', 2),
    ('paper', 'paper', 0),
    ('scissors', 'SCISSORS', 0),
]


@pytest.mark.parametrize('player1, player2, expected', testdata)
def test_run(player1, player2, expected):
    assert main.run(player1, player2) == expected
