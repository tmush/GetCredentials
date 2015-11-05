import twitter
import sys; sys.stdout.encoding; sys.stderr.encoding


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
print (us_trends)
print
print (ascii(world_trends))