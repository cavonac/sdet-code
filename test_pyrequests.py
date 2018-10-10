import requests

def test_gitevents():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200

def test_XFrameOptions():
    # Checking that OWASP.org sets the X-Frame-Options header correctly to deny clickjacking
    r = requests.get('http://www.owasp.org/')
    assert dict(r.headers).get("X-Frame-Options") == 'DENY'