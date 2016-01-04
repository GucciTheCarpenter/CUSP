import os
import sys
import datetime
from datetime import datetime
from collections import Counter, OrderedDict
import collections


def executeTweetCount(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	twit_lon = tokens[2]
	twit_lat = tokens[3]
	twit_hash = tokens[4:]
	
	global minDate
	global maxDate
		
	if twit_name in tweet_count:
		tweet_count[twit_name] += 1	
	if not twit_name in tweet_count:
		tweet_count[twit_name] = 1
		
	if twit_date < minDate:
		minDate = twit_date
	if twit_date > maxDate:
		maxDate = twit_date



def openFile(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeTweetCount(line.strip())
	

if __name__ == '__main__':
	
	tweet_count = {}
	
	minDate = datetime.strptime("9999-12-31", "%Y-%m-%d")
	maxDate = datetime.strptime("0001-01-01", "%Y-%m-%d")
	
	openFile(sys.argv[1])
	
	mostTweets = max(tweet_count.iterkeys(), key=(lambda key: tweet_count[key]))
		
	print '%s tweeted the most' % (mostTweets) + '\nDataset range: %s and %s' % (minDate.strftime('%B %d %Y, %H:%M:%S'), maxDate.strftime('%B %d %Y, %H:%M:%S'))

	
	
