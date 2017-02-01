import pandas as pd
import json
import re

file = r'C:\Users\Paul\Downloads\tweepy.txt'

tweet_data = []
tweet_file = open(file, 'r')

# 제이슨으로 된 파일을 읽어서 리스트로 일단 만들어
for line in tweet_file:
    tweet = json.loads(line)
    tweet_data.append(tweet)

tweet_file.close()

df = pd.DataFrame(tweet_data, columns=['text', 'lang'])   # 판다스 데이터 프레임으로 특정 칼럼만 뽑아서 가져옴

# print(df.head())


# 특정 글자가 몇변 나오나 카운팅을 해보자

[stock, finance] = [0, 0]

for index, row in df.iterrows():
    if re.search('stock', row['text']):
        stock += 1
    if re.search('finance', row['text']):
        finance += 1

print(stock, finance)