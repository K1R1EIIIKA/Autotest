import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# -------------------------------
# Позитивные тесты
# -------------------------------

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 5, 4),
    (0, 0, 0)
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (0, 5, -5),
    (-3, -3, 0)
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-2, 4, -8)
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-8, -2, 4)
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


# -------------------------------
# Негативные тесты
# -------------------------------

def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (1, False),
    (0, False),
    (-5, False)
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected
