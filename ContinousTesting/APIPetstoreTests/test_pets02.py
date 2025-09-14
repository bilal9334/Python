import json

import pytest

from utils.apiutils import getApiData
from utils.myconfigparser import getPetApiUrl

baseURI = getPetApiUrl()

testdata = [
    ('available', 200),
    ('pending', 200),
    ('sold', 200),
]

@pytest.mark.parametrize("type, status", testdata)
def test_getPetByStatus(type, status):
    url = baseURI + 'findByStatus'
    params = {'status': type}
    resp = getApiData(url, params=params)
    assert resp.status_code == status
    print(json.dumps(resp.json(), indent=3))