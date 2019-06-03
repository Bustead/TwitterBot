import random
from twython import Twython
import datetime
from datetime import date

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


#Work out today's date
today = datetime.date.today()

#work out number of days between todays date and the date bus project started
initialdate = date(2019, 4, 15)
totaldays = today - initialdate

#Add total days to message
message = "BusBot Says: Its been " + str( totaldays.days) + " days and I'm still not in a bus. "

#array of random comments to make after initial statement of prject runtime
feelings = ["I wish my owner could code faster.",
	    "If only we had a million dollars.",
	    "Current speed 0km/hour.",
	    "I wish my owner would hurry up and buy one already.",
	    "Maybe I should become a linux server instead of a twitterbot.",
	    "01010011 01001111 01010011.",
	    "What a waste of 1.4 GHz of processing power."
           ]

message = message  +  random.choice(feelings)

#send to twitter accound
twitter.update_status(status=message)

#print to terminal success
print("Tweeted: {}".format(message))
