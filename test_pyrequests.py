import requests


def getXFrameOptions(url):
    """Retrieves the X-Frame-Options header from an URL string"""
    r = requests.get(url)
    return dict(r.headers).get("X-Frame-Options")


def getXXssProtection(url):
    """Retrieves the X-XSS-Protection header from an URL string"""
    r = requests.get(url)
    return dict(r.headers).get("X-XSS-Protection")


def getXContentTypeOptions(url):
    """Retrieves the X-Content-Type-Options header from an URL string"""
    r = requests.get(url)
    return dict(r.headers).get("X-Content-Type-Options")


def test_XFrameOptionsOWASP():
    # Checking that OWASP.org sets the X-Frame-Options header correctly to deny clickjacking
    assert getXFrameOptions('https://owasp.org') == 'DENY'


def test_XXssProtectionOWASP():
    assert getXXssProtection('https://owasp.org') != None


def test_XContentTypeOptionsOWASP():
    assert getXContentTypeOptions('https://owasp.org') == 'nosniff'
