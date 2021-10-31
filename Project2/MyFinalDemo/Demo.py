import GoogleApi as GA
import record as Twitter
import os
####1.Enable the project after producing####
####2.Change the path in line 6, os.environ####
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\111\Desktop\project2\Final\grand-bank-330020-d28baa368690.json"
print("Welcome to my social media analyzer")
print("We can help you get the tweets and explain them based on the username you given.")
text2 = input("Please enter the Username you are looking for:")
GA.analyze_text_sentiment(Twitter.TwitAly(text2))
GA.analyze_text_entities(Twitter.TwitAly(text2))
GA.analyze_text_syntax(Twitter.TwitAly(text2))
GA.classify_text(Twitter.TwitAly(text2))
'''
The code in the following can be used to test Twitter and GoogleNLP functions independently.
Just uncomment them, run them and follow the instruction.
'''
# print("Please choose and type Twitter or Google")
# a = input("Please choose your survice:")
# if(a == "Twitter"):
#     text = input("Please enter the content you are looking for:")
#     Twitter.TwitAly(text)
#     print("The tweets have been save in the document called elon_tweets.csv!")
# elif(a == "Google"):
#     print("Please choose: sentiment OR entities OR syntax OR classify")
#     b = input("choose Google survice:")
#     if(b == "sentiment"):
#         text = input("Please enter your text:")
#         GA.analyze_text_sentiment(text)
#     elif(b == "entities"):
#         text = input("Please enter your text:")
#         GA.analyze_text_entities(text)
#     elif(b == "syntax"):
#         text = input("Please enter your text:")
#         GA.analyze_text_syntax(text)
#     elif(b == "classify"):
#         text = input("Please enter your text:")
#         GA.classify_text(text)
#     else:
#         print("Please enter in correct choice!")
# else:
#     print("Please enter in correct choice!")

