import requests
import pytest


def get_x_frame_options(url):
    """Retrieves the X-Frame-Options header from an URL string"""
    r = requests.get(url)
    return dict(r.headers).get("X-Frame-Options")


def get_x_xss_protection(url):
    """Retrieves the X-XSS-Protection header from an URL string"""
    r = requests.get(url)
    return dict(r.headers).get("X-XSS-Protection")


def get_x_content_type_options(url):
    """Retrieves the X-Content-Type-Options header from an URL string"""
    r = requests.get(url)
    return dict(r.headers).get("X-Content-Type-Options")


def test_x_frame_options_owasp():
    # Checking that OWASP.org sets the X-Frame-Options header correctly to deny clickjacking
    assert get_x_frame_options('https://owasp.org') == 'SAMEORIGIN'


@pytest.mark.skip(reason="Not working, may have changed.")
def test_x_xss_protection_owasp():
    assert get_x_xss_protection('https://owasp.org') is not None


def test_x_content_type_options_owasp():
    assert get_x_content_type_options('https://owasp.org') == 'nosniff'