import tweepy
import sys
import os
from dotenv import load_dotenv
import csv
import re

# Load credentials from .env file
load_dotenv()

"""https://stackoverflow.com/a/49986645/3711660"""
def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)

def TwitAly(text1):
    # 1. Authenticate
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
    print(CONSUMER_KEY)
    print(CONSUMER_SECRET)
    print(ACCESS_TOKEN)
    print(ACCESS_TOKEN_SECRET)
#     auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'),
#                             os.getenv('CONSUMER_SECRET'))
#     auth.set_access_token(os.getenv('ACCESS_TOKEN'),
#                         os.getenv('ACCESS_TOKEN_SECRET'))
    auth = tweepy.OAuthHandler(CONSUMER_KEY,
                                CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,
                            ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    if (not api):
        print("Authentication failed!")
        sys.exit(-1)

        # 2. Get data
    data = api.user_timeline(text1, tweet_mode="extended", count=200, exclude_replies=True)
        # 3. Save data
    x = ""
    with open('elon_tweets.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['created_at', 'text']
        writer = csv.DictWriter(csv_file, fieldnames)
        writer.writeheader()

        for tweetObject in data:
            writer.writerow({'text': deEmojify(tweetObject.full_text),
                                'created_at': tweetObject.created_at})
            ##print(f"{tweetObject.full_text}")
            x = x + f"{tweetObject.full_text}" + "\n"
    print('DONE!')
    return x
