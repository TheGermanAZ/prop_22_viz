
from api import consumer_key, consumer_secret, access_token, access_secret
import tweepy

# auth settings
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


print(tweepy.API.me(api))
