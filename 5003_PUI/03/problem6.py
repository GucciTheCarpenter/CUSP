import os
import sys
import datetime
from datetime import datetime
from collections import Counter, OrderedDict
import collections


def executeFreqHR(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	# twit_date_NoFormat = tokens[1]
	twit_lon = tokens[2]
	twit_lat = tokens[3]
	twit_hash = tokens[4:]

	tdate_hour = twit_date.strftime('%B %d %Y, %Hh')
	
	
	if tdate_hour in tweet_time_freq:
		tweet_time_freq[tdate_hour] += 1	
	if not tdate_hour in tweet_time_freq:
		tweet_time_freq[tdate_hour] = 1



def openFile(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeFreqHR(line.strip())
	

if __name__ == '__main__':
	
	tweet_time_freq = {}
	
	openFile(sys.argv[1])
	
	mostDateTime = max(tweet_time_freq.iterkeys(), key=(lambda key: tweet_time_freq[key]))
	
	print '%s with %s tweets' % (mostDateTime, tweet_time_freq[mostDateTime])

	
	
