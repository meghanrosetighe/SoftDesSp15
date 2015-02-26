#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3057582359-oeHF2ndBmOnWA05SRHU8JiXVtwFgL79XBQrnvm3"
access_token_secret = "HJmaTzGDf3He1TYlAI2pHdIJmTSFYWNq5xk83xeJBRw58"
consumer_key = "p4dTHiJFwAQHOWBW6HeuCHv2o"
consumer_secret = "xwVRqHoDwnZBs82dAYLn68Lk6CmYu3xJGkwknlB9rx7TdwnNz0"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
     #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['slytherin'])