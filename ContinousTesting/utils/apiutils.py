import json

import requests


def getApiData(url, opheader=None, params=None):
    response = requests.get(url, verify=False, headers=opheader, params=params)
    print("Request URL: " + url)
    print("request header: ", response.request.headers)
    print("request header: ", response.headers)
    return response


def postApiData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("\nReqURL:" + url)
    print("ReqBody:", json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers)
