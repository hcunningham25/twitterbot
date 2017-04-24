from twython import Twython, TwythonError

CONSUMER_KEY = 'GJ67tQw5Ws8J7wMkH8agsdAbV'
CONSUMER_SECRET = 'fImYHhTFYMoI2L3q0nWuK1GzQ1f7ySS6sxOg47zYO8wB5EHDkv'
ACCESS_TOKEN = '839153828050137088-A178qGnkQu6pLG5SFPpI6DAKmcoy9y6'
ACCESS_TOKEN_SECRET = 'vEBsuQE7XOctc8i5t8gZtlptOWQYikSu3E91HwP8336od'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv
