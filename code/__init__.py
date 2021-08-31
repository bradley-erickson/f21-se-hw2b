import requests


def call_api():
    response = requests.get("http://api.icndb.com/jokes/random?limitTo=[nerdy]")
    return response.status_code


def test_call_api():
    assert call_api() == 200
