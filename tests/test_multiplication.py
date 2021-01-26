import pytest

items = [
    (1, 2, 2),
    (1, 3, 3),
    (1, 4, 4),
    (1, 5, 5)
]


@pytest.mark.parametrize('x, y, result', items)
def test_parameter(x, y, result):
    assert x*y == result

