import os
import sys
import datetime
from datetime import datetime
from collections import Counter, OrderedDict
import collections


def withinCoord(l, x):
	if x >= l[0] and x <= l[1]:
		return True

def executeLongLat(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	twit_lon = float(tokens[2])
	twit_lat = float(tokens[3])
	twit_hash = tokens[4:]
	
	
	if withinCoord(Long_NY, twit_lon) == True and withinCoord(Lat_NY, twit_lat) == True:
		for i in twit_hash:
			hash_msg_NY.append(i)
	if withinCoord(Long_SF, twit_lon) == True and withinCoord(Lat_SF, twit_lat) == True:
		for i in twit_hash:
			hash_msg_SF.append(i)
	
	
	#for i in twit_hash:
	#	hash_msg1.append(i)


def openFile(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeLongLat(line.strip())
	

if __name__ == '__main__':
	
	hash_msg_NY = []
	hash_msg_SF = []
	
	Long_NY = [-74.2557, -73.6895]
	Lat_NY = [40.4957, 40.9176]
	Long_SF = [-122.5155, -122.3247]
	Lat_SF = [37.7038, 37.8545]
	
	openFile(sys.argv[1])
	
	hashCount_NY = Counter(hash_msg_NY).most_common(10)
	hashCount_sorted_NY = sorted(hashCount_NY, key=lambda element:(-element[1], element[0]))
	
	hashCount_SF = Counter(hash_msg_SF).most_common(10)
	hashCount_sorted_SF = sorted(hashCount_SF, key=lambda element:(-element[1], element[0]))
	
	print 'New York:'
	for i in hashCount_sorted_NY[:5]:
		print str(i[0]) + ', ' + str(i[1])
	print 'San Francisco:'
	for i in hashCount_sorted_SF[:5]:
		print str(i[0]) + ', ' + str(i[1])
