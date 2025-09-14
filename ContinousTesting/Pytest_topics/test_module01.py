from utils.myconfigparser import getPetApiUrl

BASE_URL_PETSTORE = getPetApiUrl()


def test_add():
    assert 5 + 5 == 10


def test_subtract():
    assert 5 - 2 == 3


def test_multiply():
    assert 5 * 4 == 20


def test_div():
    assert 4 / 2 == 2


# This is a failed test
def test_failing():
    assert 9 / 5 == 1.5, "Failed test intentionally"


def test_int_trunc():
    assert 9 // 5 == 1  # integer truncating division


def test_config():
    url = BASE_URL_PETSTORE + '123'
    print(url)
    assert 'petstore' in url, "String 'petstore' not found in url"
