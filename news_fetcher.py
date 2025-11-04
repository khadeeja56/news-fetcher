import requests

from bs4 import BeautifulSoup

def fetch_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []  # Return empty list if there's an issue with the request

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the headlines, this may change based on the website structure
    headlines = []
    
    # Look for headlines in the BBC News website
    for item in soup.find_all('h2', class_='sc-fa814188-3'):
        headlines.append(item.get_text())

    return headlines











