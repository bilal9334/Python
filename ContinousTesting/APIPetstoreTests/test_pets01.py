import pytest

from utils.apiutils import getApiData, postApiData
from utils.myconfigparser import getPetApiUrl

baseURI = getPetApiUrl()
petID = '191'


@pytest.fixture
def add_pet():
    url = baseURI
    payload = {"id": int(petID), "name": "Zues", "status": "available"}
    resp = postApiData(url, payload)
    pet_ID = resp.json()['id']
    print(pet_ID)
    yield pet_ID


def test_getPetByID(add_pet):
    url = baseURI + str(add_pet)
    headers = {'Content-Type': 'application/json'}
    print("RequestsURL: " + url)
    resp = getApiData(url, headers)
    assert resp.json()
    print(resp.json())
    assert resp.status_code == 200
