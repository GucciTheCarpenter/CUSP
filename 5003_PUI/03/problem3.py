import os
import datetime
from datetime import datetime
import sys


def executeHash(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	twit_lon = tokens[2]
	twit_lat = tokens[3]
	twit_hash = tokens[4:]
	
	for i in twit_hash:
		hash_msg1.append(i)
	
def executeHashCompare(tweetLine):
	tokens = tweetLine.split(',')
	twit_name = tokens[0]
	twit_date = datetime.strptime(tokens[1], '%a %b %d %H:%M:%S %Z %Y')
	twit_lon = tokens[2]
	twit_lat = tokens[3]
	twit_hash = tokens[4:]
	
	for i in twit_hash:
		if i in set(hash_msg1):
			hash_msg2.append(i)
		
		
def openFile(commandFileName1, commandFileName2):
	f1, f2 = open(commandFileName1), open(commandFileName2)
	for line in f1:
		executeHash(line.strip())
	for line in f2:
		executeHashCompare(line.strip())		
			
if __name__ == '__main__':
	
	twit_count = 0
	
	twit_users = []
	
	hash_msg1 = []
	hash_msg2 = []
		
	minDate = datetime.strptime("9999-12-31", "%Y-%m-%d")
	maxDate = datetime.strptime("0001-01-01", "%Y-%m-%d")
	
	openFile(sys.argv[1], sys.argv[2])
	
	for i in sorted(set(hash_msg2)):
		print i
	
