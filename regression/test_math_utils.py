import math_utils

def test_add_positive_numbers():
    result = math_utils.add(2, 3)
    assert result == 5

def test_add_negative_numbers():
    result = math_utils.add(-2, -3)
    assert result == -5

def test_add_mixed_numbers():
    result = math_utils.add(2, -3)
    assert result == -1

def test_add_zero():
    result = math_utils.add(0, 0)
    assert result == 0
