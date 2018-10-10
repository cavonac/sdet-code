import requests

def test_gitevents():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200