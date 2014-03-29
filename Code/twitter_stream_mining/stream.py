
import tweepy.streaming
from tweepy import OAuthHandler
from tweepy import Stream
import credentials
import atexit
import py_tweet
import sqlite3

class StdOutListener( tweepy.streaming.StreamListener):
	def on_data(self, data):
		tweet_match = py_tweet.tweet(data)

		if hashtag_filter(tweet_match.message):
			print getattr(tweet_match,'time')
			sql_insert = """
			INSERT or IGNORE
			INTO {} VALUES (?,?,?,?,?,?,?,?,?,?);
			""".format( db_name )
			db.cursor().execute( sql_insert , tweet_match.get_tuple() )
			db.commit()
		
		return True

# Requires ONE hashtag to be in the tweet.
def hashtag_OR_filter(message):
	for query in hashtag_queries:
		if query in message:
			return True
	return False

# Requres ALL hashtags to be in the tweet.
def hashtag_AND_filter(message):
	for query in hashtag_queries:
		if query not in message:
			return False
	return True

def start_record(db_name):
	sql_init = """
	CREATE TABLE if NOT EXISTS {} (
		url TEXT,
		user TEXT,
		message TEXT,
		hashtags TEXT,
		time TEXT,
		longitude REAL,
		latitude REAL,
		country TEXT,
		state TEXT,
		state_initial TEXT,
		PRIMARY KEY (url)
	);
	""".format(db_name)
	db = sqlite3.connect( 'logs/data.db' )
	atexit.register( clean_up, db )

	cursor = db.cursor()
	cursor.execute( sql_init )
	return db

# Closes database at the end of logging
def clean_up( db ):
	db.close()


if __name__ == '__main__':
	listener = StdOutListener()
	auth = OAuthHandler(credentials.consumer_key, 
		credentials.consumer_secret)
	auth.set_access_token(credentials.access_token,
		credentials.access_token_secret)
	stream = Stream(auth, listener)	

	query = str(raw_input('Enter the hashtags you would like to search for '
				+ 'separated by spaces: ')).lower()
	hashtag_queries = query.split(' ')

	search_type = str( raw_input('Should returned tweets include all or >=1 hashtags? Enter '+
		'"all" or "one"')).lower()

	if 'all' in search_type:
		hashtag_filter = hashtag_AND_filter
		db_name = '_AND_'.join(hashtag_queries)
	else:
		hashtag_filter = hashtag_OR_filter
		db_name = '_OR_'.join(hashtag_queries)
	
	print db_name
	db = start_record(db_name)

	stream.filter( track = hashtag_queries )

