
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

		if tweet_match.message:
			print getattr(tweet_match,'time')
			sql_insert = """
			INSERT or IGNORE
			INTO {} VALUES (?,?,?,?,?,?,?,?,?,?);
			""".format( db_name )
			db.cursor().execute( sql_insert , tweet_match.get_tuple() )
			db.commit()
		
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

	query = "AAP"

	db_name = query

	print db_name
	db = start_record(db_name)

	stream.filter( track = query )

