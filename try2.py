import tweepy
import requests
import json

#private information. It's given when signin up to twitter api
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
#override tweepy.StreamListener to add logic to on_status

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:

            r = requests.post("https://api.trendi.guru/images", data = json.dumps({'imageList': status.entities[u'media'][0][u'media_url_https'], 'pageUrl':"twitter"}))
            print status.entities[u'media'][0][u'media_url_https']

        except BaseException, e:
            print 'faild to print image link:', str(e)


auth = tweepy.OAuthHandler( consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=["fashion"])