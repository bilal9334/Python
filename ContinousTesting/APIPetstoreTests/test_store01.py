import pytest

from utils.apiutils import getApiData, postApiData
from utils.myconfigparser import getStoreApiUrl

baseURI = getStoreApiUrl()
orderID = 3


def test_getPetByID():
    url = baseURI + '/' + str(orderID)
    headers = {'Content-Type': 'application/json'}
    print("Request URL: " + url)
    resp = getApiData(url, headers)
    assert resp.json()
    print(resp.json())
    assert resp.status_code == 200
