from twython import Twython
import csv

from collections import Counter


CONSUMER_KEY = 'R2pWRXsbIvXqkHxljWC7muqf4'
CONSUMER_SECRET = 'RIPuyuK8wdd81M23xDqxSWUiwcBaQO5q4TbkfiqIEAIq8T4x1C'
ACCESS_TOKEN = '2806069908-UMVC9dsiI4gMqSBdDSKU1YiJ1fG8gOV0YY0dqCx'
ACCESS_TOKEN_SECRET = 'F93y3Nn9wgaPG91iX1Gm3nPsy5jrZCa00dVIYkYabLK8I'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='#InfiniteKusama', count="500")

tweets = search['statuses']

c = Counter (#InfiniteKusama, #YayoiKusama)


c['#InfiniteKusama'] += 1
c
Counter({'#InfiniteKusama': 1})

c = Counter('#InfiniteKusama','#YayoiKusama',)
Counter({'#InfiniteKusama':1, '#YayoiKusama':2})

with open ('test4.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('#InfiniteKusama', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['#InfiniteKusama', result['text'].encode('utf-8'), url]]
        a.writerows((text))




