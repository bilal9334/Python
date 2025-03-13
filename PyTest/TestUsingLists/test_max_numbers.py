import pytest
from max_number import find_max

def test_find_max():

    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([10, 20, 30]) == 30
    assert find_max([-5, -1, -10]) == -1
    assert find_max([100]) == 100
    assert find_max(range(1,51)) == 50