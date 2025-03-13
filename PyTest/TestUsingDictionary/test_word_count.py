import pytest
from word_count import word_count

def test_word_count():
    assert word_count("Python is fun") == {"python": 1, "is": 1, "fun": 1}
    assert word_count("") == {}