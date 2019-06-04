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

#ask user for message
user_input = raw_input("What would you like BusBot to say? ")

#put userinput into a message
message = ("BusBot Says: " + user_input)

#send to twitter accound
twitter.update_status(status=message)

#print to terminal success
print("Tweeted: {}".format(message))
