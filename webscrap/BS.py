from bs4 import BeautifulSoup
import requests

url = 'https://iottechnews.com'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.106 Chrome/68.0.3440.106 Safari/537.36'}

response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content,'lxml')
div = soup.find('div', id = 'latest-container')
print(div)