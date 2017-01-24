import requests

# urllib 대신 한번에 가져올수 있는 패키지 인데, 구글도 쓰고 많이 쓰는 팩이라고 함
# 훨씬 정리된 형태로 보여줌 시간은 더 오래걸리는듯?

url = 'https://www.codecademy.com/learn/all'

r = requests.get(url)  # 리퀘스트와 리스폰스를 한번에 할수 있는 함수

text = r.text  # urllib의 read() 대신에 text() 로 html 읽어옴

print(text)