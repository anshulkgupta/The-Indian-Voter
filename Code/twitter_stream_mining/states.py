
import sqlite3

state_population = {'California':36457549,'Texas':23507783,'New York':19306183,'Florida':18089888,'Pennsylvania':12831970,'Illinois':12440621,'Ohio':11478006,'Georgia':10095643,'North Carolina': 9363941,'Virginia': 8856505,'Michigan': 8724560,'New Jersey': 7642884,'Washington': 6437193,'Massachusetts': 6395798,'Arizona': 6313520,'Maryland': 6166318,'Tennessee': 6038803,'Indiana': 5710678,'Wisconsin': 5580000,'Colorado': 5556506,'Missouri': 5167101,'Minnesota': 5053377,'South Carolina': 4599030,'Kentucky': 4321249,'Alabama': 4287768,'Connecticut': 4206074,'Nevada': 3700758,'Oregon': 3579212,'Louisiana': 3504809,'Iowa': 2982085,'Oklahoma': 2910540,'Mississippi': 2810872,'Kansas': 2764075,'Arkansas': 2550063,'Utah': 2495529,'New Mexico': 1954599,'Maine': 1818470,'New Hampshire': 1768331,'West Virginia': 1466465,'Nebraska': 1321574,'Hawaii': 1314895,'Idaho': 1285498,'South Dakota': 1067610,'Rhode Island':  944632,'Montana':  853470,'Alaska':  781919,'North Dakota':  640567,'Delaware':  635867,'Vermont':  623908,'Wyoming':  515004, 'Washington, D.C.': 632323}


db = sqlite3.connect( 'logs/data.db' )
cursor = db.cursor()

cursor.execute( """
SELECT 
	name
FROM 
	sqlite_master 
WHERE
	sql NOT NULL;""" )
table_list = cursor.fetchall()

for table in table_list:
	table = table[0].encode('ascii','ignore')
	print '\nTable: ',table
	sql_query = """
	SELECT
		COUNT(url),
		state
	FROM
		{}
	WHERE
		country is 'United States' AND
		state not NULL AND 
		state_initial not NULL
	GROUP BY
		state
	ORDER BY
		COUNT(url) desc;
	""".format(table)

	for row in cursor.execute(sql_query):
		state = row[1].encode('ascii','ignore')
		relative_frequency = 1.0*row[0]/state_population[state]*1000000
		print row[0],'\t',relative_frequency,'\t',state


cursor.close()
db.close()
