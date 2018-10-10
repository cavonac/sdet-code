import requests
def getXFrameOptions(url):
    r = requests.get(url)
    return dict(r.headers).get("X-Frame-Options")

def test_XFrameOptionsOWASP():
    # Checking that OWASP.org sets the X-Frame-Options header correctly to deny clickjacking
    assert getXFrameOptions('https://www.owasp.org/') == 'DENY'