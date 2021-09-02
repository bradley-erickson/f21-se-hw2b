#! /bin/python
import requests


def call_api():
    response = requests.get("http://api.icndb.com/jokes/random?limitTo=[nerdy]")
    return response.status_code, response.content

if __name__ == '__main__':
    status, content = call_api()
    print(content)
