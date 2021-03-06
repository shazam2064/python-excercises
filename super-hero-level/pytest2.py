import pytest


# Function to be tested
def my_func(x, y, z):
    return x + y + z


# Function to be tested
def my_exception():
    div = 10 / 0
    return div


# Grouping tests inside a class prefixed with 'Test'; the functions should also be prefixed with 'test'
class TestClass(object):
    def test_result1(self):
        assert my_func(1, 2, 3) == 5

    def test_result2(self):
        assert my_func(1, 2, 3) == 6


def test_result3(self):
    with pytest.raises(ZeroDivisionError):
        my_exception()
