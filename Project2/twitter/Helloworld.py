import tweepy
import sys
import os
from dotenv import load_dotenv
import csv
import re

#load_dotenv()
CONSUMER_KEY = "Please enter key"
CONSUMER_SECRET = "Please enter secret"
ACCESS_TOKEN = "please enter token"
ACCESS_TOKEN_SECRET = "please enter token secret"
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'),
                           os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'),
                      os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

########Please choose any case to run##############
####Case 1######
# print('Case 1')
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print("1111")
#     print(tweet.text)

###Case 2###########
# print('Case 2')
# user = api.get_user('narendramodi')
# print(user.screen_name)
# print(type(user.followers_count))
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

####Case 3###########
# print('Case 3')
# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.follow())

####Case 4###########only deal with one page tweets
# print('Case 4')
# user = tweepy.Cursor(api.user_timeline, id="twitter")
# for items in user.items(10):
#     print(items)

# for page in user.pages(2):
#     print(page)

####Case 5###########
# print('Case 5')
# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self,status):
#         print(status.text)

#     def on_error(self,status_code):
#         print(status_code)
#         if status_code == 420:
#             return False

# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# myStream.filter(track=['python']) ## Use track for key word
# myStream.filter(follow=["2211149702"]) ## Use follow for specfic twitter ID