import requests
from bs4 import BeautifulSoup

url = 'https://campus.datacamp.com/courses/introduction-to-relational-databases-in-python/applying-filtering-ordering-and-grouping-to-queries?ex=12900'

r = requests.get(url)

html = r.text

soup = BeautifulSoup(html, 'html.parser')

# lxml 요거를 넣던지 'html.parser' 넣어야지 경고 메세지 않뜨는데 원인은 좀 찾아봐야할듯함...

pretty_soup = soup.prettify()

# print(pretty_soup)

print(soup.title)  # 제목부분만 가져오는 명령
print(soup.get_text())  # text 만 뽑아 오는 방법 (?)

a_tag = soup.find_all('a')  # href 만 뽑아오는방법
for link in a_tag:
    print(link.get('href'))