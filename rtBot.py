import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q="#Endsars").items():
    try:
        print("\nTweet by: @" + tweet.user.screen_name)

        tweet.retweet()
        print("Retweeted the tweet")

        # Favorite the tweet
        tweet.Like()
        print("Liked the tweet")

        

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break