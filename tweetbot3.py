import requests
from twython import Twython
import csv

CONSUMER_KEY = 'GJ67tQw5Ws8J7wMkH8agsdAbV'
CONSUMER_SECRET = 'fImYHhTFYMoI2L3q0nWuK1GzQ1f7ySS6sxOg47zYO8wB5EHDkv'
ACCESS_TOKEN = '839153828050137088-A178qGnkQu6pLG5SFPpI6DAKmcoy9y6'
ACCESS_TOKEN_SECRET = 'vEBsuQE7XOctc8i5t8gZtlptOWQYikSu3E91HwP8336od'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='YOUR SEARCH TERM HERE', count="100")
tweets = search['statuses']

r = requests.get("https://analytics.usa.gov/data/live/realtime.json")
r.json()['data'][0]['active visitors']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
           twitter.update_status(status='Active Visitors: %' % r.json () ['data'][0]
    text=[['Kusama', '#InfiniteKusama', result['text'].encode('utf-8'), url]]
        a.writerows((text))
