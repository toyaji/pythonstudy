import tweepy
import json
from Datacamp.API.MyStreamListener import MyStreamListener

# 트위터 앱 접근 관련 정보
access_token = "824792164802523138-J6x7XDjo9lFdrtNISLylX6tVNobm8rE"
access_token_secret = "0EAgqnbRBWTLFHSff8BxAsjmrvFgyC86TWi1ZzuuhreRg"
consumer_key = "QBv5ia1nvbsVRIzCfDG8u2bkB"
consumer_secret = "WXzcd5OZnVj233yY7skpGFB6fSgjJ58YKeH4wEh1vf46JKiWOz"

# OAtuth 인증 관련 함수 (트위피 내장함수)
auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# 스트림리스너로 트위터 읽어서 가져오는 건데... 이 부분은 함수 좀 더 뜯어봐야함..ㅠ
file = r'C:\Users\Paul\Downloads\tweepy.txt'
listener = MyStreamListener(file)          # 데이터캠프에서 트윗 제이슨 받는 방식 바꾼 클래스 그대로 가져다가 씀
stream = tweepy.Stream(auth, listener)

stream.filter(track=['stock', 'finance'])


tweet_data = []
tweet_file = open(file, 'r')

for line in tweet_file:
    tweet = json.loads(line)
    tweet_data.append(tweet)

tweet_file.close()

print(tweet_data[0].keys())


"""집에서 가상에서는 판다스가 안되고 로컬에서는 트위피(tweepy)가 인스톨이 안되서 파일 두개로 쪼개서 후반부 진행함"""