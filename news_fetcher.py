import requests
from bs4 import BeautifulSoup

def fetch_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for tag in soup.find_all('a', href=True):
        # Many BBC links start with /news/, we’ll filter those
        if tag.get('href').startswith('/news/') and tag.find('h2'):
            headline_text = tag.get_text().strip()
            link = "https://www.bbc.com" + tag.get('href')
            headlines.append({'title': headline_text, 'link': link})

    # Remove duplicates
    unique = []
    seen = set()
    for h in headlines:
        if h['title'] not in seen:
            unique.append(h)
            seen.add(h['title'])
    
    return unique
      













