import tweepy

api_key = "HbzSwgYLJvd7owWdftoqeaUAx"
api_secret = "PyUZrlcJpC3Seyv9bKxWin5IpGNfpO1O81dDUWbw5FypplmnCu"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAHo0rQEAAAAAfCs%2BsiYl6HmZhawdMsacwp0fxuw%3DeVAff3KwSoK6VSnGxc8lcmowyqIt01qI7ltVWGLvr4NGt2yc3d"
access_token = "1417383526119346176-K9CDHLEx4eNHqo0z20LDls6QODbGam"
access_token_secret = "gW7X2JPSgTiC4fMHYh6ESNBPrJ8IUkUolGoHEXsnuHCkM"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# client.create_tweet(text ="TIMSCDR")

# client.like("1731334971195830698")

# client.retweet("1731334971195830698")

# Client.create_tweet(in_reply_to_tweet_id="1734138809057517728", text = "WELCOME TO MCA")

# for tweet in api.home_timeline():
    #print(tweet.text)

# person = client.get_user(username = "narendramodi").data.id

# for tweet in client.get_users_tweets("narendramodi").data:
    # print(tweet.text)


