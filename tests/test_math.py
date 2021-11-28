"""
This module contains the basic unit tests for math operations.
"""

import pytest

# -------------------------------------------------------
# A basic math function
# -------------------------------------------------------

@pytest.mark.math
def test_one_plus_one():
    assert 1+1 == 2 

@pytest.mark.math
def test_one_minus_one_success_():
    assert 1-1 == 0

@pytest.mark.math
def test_divivde_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)

products = [
    (2, 3, 6),           # positive scenario
    (1, 80, 80),         # identity
    (0, 80, 0),          # zero
    (2, -3, -6),         # positive by negative
    (-2, -2, 4),         # negative by negative
    (2.5, 3.5, 8.75),    # float by float
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product