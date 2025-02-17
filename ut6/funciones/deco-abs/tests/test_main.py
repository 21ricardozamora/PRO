import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (3, 2, 5),
    (-3, -2, 5),
    (3, -2, 5),
    (-3, 2, 5),
]


@pytest.mark.dependency()
def test_decorator_exists():
    assert getattr(main, 'fabs', None), 'El decorador debe llamarse fabs'


@pytest.mark.parametrize('x, y, expected', testdata)
@pytest.mark.dependency(depends=['test_decorator_exists'])
def test_expected(x, y, expected):
    deco_func = main.fabs(lambda a, b: a + b)
    assert deco_func(x, y) == expected
