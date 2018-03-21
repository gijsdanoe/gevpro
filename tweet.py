

import tweepy
from keys import *

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey, asecret)

api = tweepy.API(auth)

api.update_status('Dit is een mooi voorbeeld van een zeventiensyllabige haiku')
