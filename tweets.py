# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '349383826-NGP5MtMxnrFM7sizHzKA66CkotPeKTXNY7qla1c2'
ACCESS_SECRET = 'KrM3tkJQ3RF3fHSYBHz1oO5eNukUuA0aAC58qjmtTmgUL'
CONSUMER_KEY = 'fLwB8QL7VxB7Ow1G52O5Umu0P'
CONSUMER_SECRET = 'XTNRS9bqm0FEXT8O1oWEiaGCwi5Um20JDYPg8dUocZZW8wlECs'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


tweets = tweepy.Cursor(api.search, q='#Target', lang = 'en', count=5000).items(5000)
i = 0
for status in tweets:
    try:
        i +=1
        word = str(status._json)
        word = word.replace("\'", "\"")
        word.encode('ascii', 'ignore')
        print(word[word.index("text") +8: word.index("truncated", word.index("text"))-4])
    except:
        pass

#for status in tweepy.Cursor(api.home_timeline).items(200):
#    print(status._json)

#library json or simplejson to read in the data in JSON format and process them:

# Import the necessary package to process data in JSON format
'''
try:
    import json
except ImportError:
    import simplejson as json

tweets = open("tweets.txt", "r")
for line in tweets:
    print(line)
'''
