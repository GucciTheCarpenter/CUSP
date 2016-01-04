import os
import sys
import datetime
from datetime import datetime
from collections import Counter, OrderedDict
import collections


def executeFreqSec(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	twit_lon = tokens[2]
	twit_lat = tokens[3]
	twit_hash = tokens[4:]

	if twit_date in tweet_time_freq:
		tweet_time_freq[twit_date] += 1	
	if not twit_date in tweet_time_freq:
		tweet_time_freq[twit_date] = 1



def openFile(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeFreqSec(line.strip())
	

if __name__ == '__main__':
	
	tweet_time_freq = {}
	
	openFile(sys.argv[1])
	
	mostDateTime = max(tweet_time_freq.iterkeys(), key=(lambda key: tweet_time_freq[key]))
	
	print '%s with %s tweets' % (mostDateTime.strftime('%B %d %Y, %H:%M:%S'), tweet_time_freq[mostDateTime])
	
	
	
