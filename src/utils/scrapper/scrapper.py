def get_session(url):
    from requests_html import HTMLSession
    session = HTMLSession()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    }
    response = session.get(url, headers=headers)
    # response.html.render()
    return response.html.html


def get_soup(response):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response, "html.parser")
    return soup
