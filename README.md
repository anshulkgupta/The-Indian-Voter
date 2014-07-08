Twitter Data Mining (primarily for geolocation data)
=====

Data scraping project - General Elections India '14 powered by the Global Education and Leadership Foundation (tGELF). This was a part of the larger project called the Indian Voter, aimed at tracking the Indian General Elections and spreading awareness using social media platforms all across India ahead of the 800+ million voters' mandate.

This python code does the following:

1. Search streaming API for hashtags pertaining to each popular political party and their leaders.
2. Check if tweet has geo location data.
3. If yes, then push it to mysql database containing tweet handle, message, geolocation data, hashtags used.
4. Export db file and use D3 / CartoDb to map it.

The project was executed under the supervision of Debarghya Das (Deedy) and the results can be found here: http://theindianvoter.com/twitter.html
