import requests
from bs4 import BeautifulSoup


def get_post_titles():
    url = 'https://www.reddit.com/r/Python/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # Send GET request
    response = requests.get(url, headers=headers)

    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all post titles (inside <h3> tags on Reddit)
    post_titles = soup.find_all('h3')

    # Extract text from the <h3> tags and return it
    titles = [post.get_text() for post in post_titles]
    return titles
