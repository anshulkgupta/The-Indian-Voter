import twitter
import json


# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'fTVGqEOwEtS5jCSV2ZA'
CONSUMER_SECRET = '5epDQkOVCUMhSc2f7JK4Gw3uJ63hPEtMIdAAzDOptE'
OAUTH_TOKEN = '604597818-dkfIvsfKdukbqe1Ay1KvZq4k0NcrEv5hYw4qj86B'
OAUTH_TOKEN_SECRET = '4MLU0w8kCoGkCmtw8sOtNspqBOfO33Wcdg5mkq73JGt51'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

# Obtain intersection of the two trends -- determine common trends
world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']]) 

common_trends = world_trends_set.intersection(us_trends_set)

print common_trends

print json.dumps(world_trends, indent=1)
print
print json.dumps(us_trends, indent=1)