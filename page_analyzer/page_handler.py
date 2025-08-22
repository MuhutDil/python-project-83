import requests
from bs4 import BeautifulSoup


def get_content(url):
    """
    Retrieves specific content elements from the provided URL
    and returns a dictionary with the results.

    Parameters:
    url (str): The URL from which to extract content.

    Returns:
    dict: A dictionary containing the status code, h1 tag text,
    title text, and description content.
    """
    TIME_ANSWER = 10
    response = requests.get(url, timeout=TIME_ANSWER)
    requests.Response.raise_for_status(response)

    soup = BeautifulSoup(response.content, "html.parser")

    status_code = response.status_code
    h1 = soup.find('h1').text if soup.find('h1') else ''
    title = soup.find('title').text if soup.find('title') else ''
    meta_description = soup.find('meta', {'name': "description"})
    description = meta_description["content"] if meta_description else ''

    return {'status_code': status_code,
            'h1': h1,
            'title': title,
            'description': description}
