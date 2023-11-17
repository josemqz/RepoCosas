# https://j2logo.com/python/web-scraping-con-python-guia-inicio-beautifulsoup/

import requests
from bs4 import BeautifulSoup

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
url = "https://j2logo.com/python/web-scraping-con-python-guia-inicio-beautifulsoup/"
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')

print(soup)
