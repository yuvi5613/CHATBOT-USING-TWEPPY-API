import tweepy
import time

api_key = "HbzSwgYLJvd7owWdftoqeaUAx"
api_secret = "PyUZrlcJpC3Seyv9bKxWin5IpGNfpO1O81dDUWbw5FypplmnCu"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAHo0rQEAAAAAfCs%2BsiYl6HmZhawdMsacwp0fxuw%3DeVAff3KwSoK6VSnGxc8lcmowyqIt01qI7ltVWGLvr4NGt2yc3d"
access_token = "1417383526119346176-K9CDHLEx4eNHqo0z20LDls6QODbGam"
access_token_secret = "gW7X2JPSgTiC4fMHYh6ESNBPrJ8IUkUolGoHEXsnuHCkM"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try: 
            client.like(tweet.id)
            
        except Exception as error:
            print(error)
            
        time.sleep(1)
        
        
    
stream = MyStream(bearer_token = bearer_token)

rule = tweepy.StreamRule("(Virat Kohli OR #python)(-is:retweet -is:reply)" )

stream.add_rules(rule)

stream.filter()