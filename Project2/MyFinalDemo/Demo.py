import GoogleApi as GA
import record as Twitter
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"savvy-mantis-327220-32c9708cc2b6.json"
print("Welcome to my social media analyzer")
print("Please choose and type Twitter or Google")
a = input("Please choose your survice:")
if(a == "Twitter"):
    text = input("Please enter the content you are looking for:")
    Twitter.TwitAly(text)
    print("The tweets have been save in the document called elon_tweets.csv!")
elif(a == "Google"):
    print("Please choose: sentiment OR entities OR syntax OR classify")
    b = input("choose Google survice:")
    if(b == "sentiment"):
        text = input("Please enter your text:")
        GA.analyze_text_sentiment(text)
    elif(b == "entities"):
        text = input("Please enter your text:")
        GA.analyze_text_entities(text)
    elif(b == "syntax"):
        text = input("Please enter your text:")
        GA.analyze_text_syntax(text)
    elif(b == "classify"):
        text = input("Please enter your text:")
        GA.classify_text(text)
    else:
        print("Please enter in correct choice!")
else:
    print("Please enter in correct choice!")

