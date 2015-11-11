import twitter
import sys; sys.stdout.encoding; sys.stderr.encoding
import json


CONSUMER_KEY = 'pIL4NYPIiEJu2KatZsNtLnIVB'
CONSUMER_SECRET = 'FG4nn9ndk0JcSX6qih32kkSTCj58Xnzjvo9AaluRY5esTqDleq'
OAUTH_TOKEN = '1711669075-ITDnvdQiWPEKXCLMZAlDACYDHkSg4pEX2Qn8Nro'
OAUTH_TOKEN_SECRET = 'TM2F5iKT0CGuC1HTSDYc5BRtq4VPP7J0zWkN36NRMyQcv'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
# Nothing to see by displaying twitter_api except that it's now a
# defined variable
print (twitter_api)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
#print (ascii(us_trends))
#print
#print (ascii(world_trends))

#print (json.dumps(us_trends, indent=1))
#print
#print (json.dumps(world_trends, indent=1))

world_trends_set = set([trend['name']
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                        for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

#print (common_trends)

q = '#Microsoft'

count = 100

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

print (json.dumps(statuses, indent=1))