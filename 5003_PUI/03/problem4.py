import os
import sys
import datetime
from datetime import datetime
from collections import Counter, OrderedDict
import collections


def executeHash(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	twit_lon = tokens[2]
	twit_lat = tokens[3]
	twit_hash = tokens[4:]
	
	for i in twit_hash:
		hash_msg1.append(i)


def openFile(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeHash(line.strip())
	

if __name__ == '__main__':
	
	hash_msg1 = []
	
	openFile(sys.argv[1])
	
	hashCount = Counter(hash_msg1).most_common(15)
	hashCount_sorted = sorted(hashCount, key=lambda element:(-element[1], element[0]))
	
	
	for i in hashCount_sorted[0:10]:
		print str(i[0]) + ', ' + str(i[1])
