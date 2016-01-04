import os
import datetime
from datetime import datetime
import sys


def executeUnique(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	twit_lon = tokens[2]
	twit_lat = tokens[3]
	twit_hash = tokens[4:]
	
	global twit_count
	global minDate
	global maxDate
	
	twit_count += 1
	
	twit_users.append(twit_name)
			
	if twit_date < minDate:
		minDate = twit_date
	if twit_date > maxDate:
		maxDate = twit_date
		
		
def openFile(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeUnique(line.strip())		
			
if __name__ == '__main__':
	
	twit_count = 0
	
	twit_users = []
		
	minDate = datetime.strptime("9999-12-31", "%Y-%m-%d")
	maxDate = datetime.strptime("0001-01-01", "%Y-%m-%d")
	
	openFile(sys.argv[1])
	
	print '%s users tweeted between %s and %s' % (str(len(set(twit_users))), minDate.strftime('%B %d %Y, %H:%M:%S'), maxDate.strftime('%B %d %Y, %H:%M:%S'))
