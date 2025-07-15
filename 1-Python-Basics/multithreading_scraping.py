import threading 
import requests
from bs4 import BeautifulSoup 

urls = [
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f'Fetched {len(soup.text)} characters from {url}')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching {url}: {e}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))  # Added comma!
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages scraped.")