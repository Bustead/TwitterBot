from twython import Twython, TwythonError
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


#useful link for more info https://www.silkstream.net/blog/2014/06/retweeting-with-your-twython-twitter-bot.html

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

search_results = twitter.search(q="roadtrip", count=1)

try:
    for tweet in search_results["statuses"]:
        twitter.retweet(id = tweet["id_str"])
except TwythonError as e:
    print e
