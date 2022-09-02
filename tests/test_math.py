import pytest

# Basic testing files
@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

@pytest.mark.math
def test_divide_by_zero():
    # Using pytest here sets the zero devision test fail as a pass, 
    # since its now testing for if theres a zero-division-error
    with pytest.raises(ZeroDivisionError) as e:
        num = 2 / 0
    assert 'division by zero' in str(e.value)

@pytest.mark.math
def test_this_fails():
    a = 1
    b = 2
    c = 3
    assert a + b == c

# Multiplication test ideas
# Two positive integers
# Is a number times 1 itself?

# DRY = Don't repeat yourself
@pytest.mark.math
def test_multiply_two_positives():
    assert 2 * 2 == 4

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0,99,0),
    (3, -4, -12),
    (-5, -4, 20),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a, b, product', products)
def test_nmultiplication(a, b, product):
    assert a * b == product
