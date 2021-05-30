"""
Fetches all tweets from certain account talking about a certain crypto
"""
# %%
import tweepy
from read_api_keys import consumer_key, consumer_secret, access_key, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)

