import sys
import tweepy

access_key = '604597818-dkfIvsfKdukbqe1Ay1KvZq4k0NcrEv5hYw4qj86B'
access_secret = '4MLU0w8kCoGkCmtw8sOtNspqBOfO33Wcdg5mkq73JGt51'

consumer_key = 'fTVGqEOwEtS5jCSV2ZA'
consumer_secret = '5epDQkOVCUMhSc2f7JK4Gw3uJ63hPEtMIdAAzDOptE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['curiosity'])	