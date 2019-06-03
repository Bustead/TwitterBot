import random
from twython import Twython

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


feelings = ["My owner is giving me some upgrades soon"
           ]

message ="BusBot says: " +  random.choice(feelings)
twitter.update_status(status=message)
print("Tweeted: {}".format(message))
