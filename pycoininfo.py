#/usr/bin/env python

# This is the python script that fetches Bitcoin and other altcoin 
# details and updates your twitter account with the details.

import coinmarketcap
import tweepy 
import sys
from datetime import datetime

# To prevent Twitter and tweepy throwing duplication errors we will
# create a timestamp to make the post unique.
i = datetime.now()
now = i.strftime('%H:%M:%S')

# Consumer keys and access tokens, used for OAuth 
# Please use your own personal information here. 
consumer_key = ''  
consumer_secret = ''  
access_token = ''  
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret) 

api = tweepy.API(auth) 

if len(sys.argv) >= 2:
	x = coinmarketcap.coin_summary(sys.argv[1])
	update_tweet = 'The current price of #' + sys.argv[1] + ' is ' + x['price'] + ' @ ' + now
else: 
	x = coinmarketcap.coin_summary('bitcoin') 
	update_tweet = 'The current price of #bitcoin is ' +  x['price'] + ' @ ' + now

api.update_status(update_tweet) 
