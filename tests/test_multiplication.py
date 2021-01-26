import pytest

items = [
    (1, 2, 2),
    (1, 2, 20),
    (1, 2, 2),
    (1, 2, 4)
]


@pytest.mark.parametrize('x, y, result', items)
def test_parameter(x, y, result):
    assert x*y == result


@pytest.mark.math
def test_skipp_keyword():
    assert 1==2