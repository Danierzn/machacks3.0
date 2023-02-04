from socialreaper import Twitter
from socialreaper.tools import to_csv

user = input("Enter your User: ")

twt = Twitter(api_key = "xxx", api_secret = "xxx", access_token = "xxx", access_token_secret = "xxx")
    
tweets = twt.user(f"{user}", count=100, exclude_replies=True, 
    include_retweets=False)
    
to_csv(list(tweets), filename=f'{user}.csv')