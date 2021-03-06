# Run this in pytest
import pytest


def my_exception():
    div = 10 / 0


def test_result1():
    with pytest.raises(ZeroDivisionError):
        my_exception()
