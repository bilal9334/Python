import pytest
from common_in_sets import find_common

def test_find_common():

    assert find_common({1,3,4,5,8}, {2,4,5,10,3}) == {3,4,5}