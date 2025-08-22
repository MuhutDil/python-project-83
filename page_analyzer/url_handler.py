from urllib.parse import urlparse

import validators


class URLValidationErrors(Exception):
    pass


class URLNotValid(URLValidationErrors):
    pass


class URLTooLong(URLValidationErrors):
    pass


def validate(url):
    """
    Checks if the provided URL is valid and within the maximum length allowed.

    Parameters:
    url (str): The URL to be checked.

    Raises:
    URLTooLong: If the URL length exceeds the maximum allowed length.
    URLNotValid: If the URL is not a valid URL.

    Returns:
    None
    """
    MAX_LENGTH_URL = 255
    if len(url) > MAX_LENGTH_URL:
        raise URLTooLong()
    if not validators.url(url):
        raise URLNotValid()


def normalize_url(url):
    """
    Clears the URL by extracting and returning the scheme and netloc parts.

    Parameters:
    url (str): The URL to be cleared.

    Returns:
    str: The cleared URL containing only the scheme
    and netloc parts(https://www.example.com).
    """
    parse_url = urlparse(url)
    return f'{parse_url.scheme}://{parse_url.netloc}'