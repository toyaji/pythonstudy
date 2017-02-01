import tweepy
import json

class MyStreamListener(tweepy.StreamListener):
    """DataCamp 에서 나오는 Hugo 가 만든 리스너 커스텀 한거를 살짝 바꾼거임..."""
    def __init__(self, file, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open(file, 'w')

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)