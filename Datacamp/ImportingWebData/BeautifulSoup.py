import requests
from bs4 import BeautifulSoup

url = 'https://www.codecademy.com/learn'

r = requests.get(url)

html = r.text

soup = BeautifulSoup(html)

pretty_soup = soup.prettify()

print(pretty_soup)