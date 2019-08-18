from twython import Twython, TwythonError
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#useful link for more info https://www.silkstream.net/blog/2014/06/retweeting-with-your-twython-twitter-bot.html

#Let's gather a list of words we DON'T want to RT
naughty_words = [" -RT", "church", "faith", "god", "politician", "terrorism"]

#And a list of words we WOULD like to RT
good_words = ["skoolie", "bus conversion", "bus", "van conversion", "tinyhouse", "tinyhome"]

#OR is Twitter's search operator to search for this OR that
#So let's join everything in good_words with an OR!
filter = " OR ".join(good_words)

# The - is Twitter's search operator for negative keywords
# So we want to prefix every negative keyword with a -
blacklist = " -".join(naughty_words)

#And finally our list of keywords that we want to search for
#This will search for any words in good_words minus any naughty_words
keywords = filter + blacklist

#This time we want to set our q to search for our keywords
search_results = twitter.search(q=keywords, count=1)
try:
    for tweet in search_results["statuses"]:
        try:
	    twitter.create_favorite(id = tweet["id_str"])
        except TwythonError as e:
            print e
except TwythonError as e:
    print e
  


