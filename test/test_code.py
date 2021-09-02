from code.call import call_api

def test_call_api():
    status, content = call_api()
    assert status == 200
