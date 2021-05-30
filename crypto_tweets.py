"""
Fetches all tweets from certain account talking about a certain crypto
"""
# %%
import tweepy
import csv
from read_api_keys import consumer_key, consumer_secret, access_key, access_secret
import time
from pandas import DataFrame
import pandas as pd
import re

def create_tweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    userID = "elonmusk"
    tweets = api.user_timeline(screen_name=userID, 
                            count=1000,
                            include_rts = False,
                            tweet_mode = 'extended')
    all_tweets = []
    all_tweets.extend(tweets)
    oldest_id = tweets[-1].id
    try:
        while True:
            time.sleep(1.1)
            tweets = api.user_timeline(screen_name=userID, 
                                count=2000,
                                include_rts = False,
                                max_id = oldest_id - 1,
                                tweet_mode = 'extended')
            all_tweets.extend(tweets)
            oldest_id = all_tweets[-1].id
            print('N of tweets downloaded till now {}'.format(len(all_tweets)))
    except KeyboardInterrupt:
        pass


    outtweets = [[tweet.created_at,
                tweet.full_text.encode("utf-8").decode("utf-8")] 
                for idx,tweet in enumerate(all_tweets)]
    df = DataFrame(outtweets,columns=["created_at", "text"])
    df.to_csv('%s_tweets.csv' % userID,index=False)
    print(df.head(3))


def keep_tweets(keywords, user):
    keep = []
    df = pd.read_csv(user + "_tweets.csv")
    for key in keywords:
        keep.append(df[df['text'].str.contains(key)])
        
    out = pd.concat(keep)

    return out

def clean_tweet(tweet_str):
    """ Return a cleaned out tweet string """
    tweet_str = re.sub(r"&amp;","and",tweet_str) # Replace & by and
    tweet_str = re.sub(r"@\S*|http\S*|[^\w ,!:;’.()]*","",tweet_str)
                #Remove @xxx   links  everything too special
    return tweet_str
        
    # %%

if __name__ == "__main__":
    testStr = "@WholeMarsBlog Not sure who wrote this, but it’s accurate https://t.co/gRvWxOJZ56 🤣🤣 @Tesmanian_com 🇩🇪 🚘 ♥️ Geil! ♥️ 🚘 🇩🇪"
    print("Before ", testStr)
    print("After ",clean_tweet(testStr))