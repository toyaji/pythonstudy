from urllib.request import urlopen, Request

url = 'https://www.codecademy.com/learn/all'

request = Request(url)  # 해당 url 로 요청을 보냄
response =  urlopen(request)  # 요청에 대한 응답을 받아

html = response.read()  # 해당 응답에 html 이 담겨 있으니까 읽어오기

print(html)

response.close()