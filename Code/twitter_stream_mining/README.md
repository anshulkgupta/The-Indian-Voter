Twitter Stream Mining
=====================
Filters the live stream of tweets. Input the hashtag(s) you're interested in and see what the world is saying with them.

Run stream.py to log tweets into the sqlite database.

	python stream.py

Run states.py to view state by state stats on the geo encoded tweets that you have gathered.

	python states.py

To Run
=====================

	// Fill out the credentials.py with your credentials
	// While in the directory:
	virtualenv --no-site-packages .
	pip install -r requirements.txt
	python stream.py
	

Goals
=====================

- [x] multiple hashtag searches
- [x] seach by geographic area
- [ ] search for all tweets mentioning a user(s)
- [ ] add qualifiers like follower count or total tweet count
- [x] populate database as opposed to writing to text file
- [ ] GUI


