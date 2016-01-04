import csv
import os
import sys

csvFile = sys.argv[1]

def openFile(filename):
	with open(filename) as f:
		csvReader = csv.reader(f)
		headers = next(csvReader)
		
		CompType = {}
		
		for row in csvReader:
			uniqueKey = row[0]
			complaintType = row[5]
			
			if not complaintType in CompType:
				CompType[complaintType] = 1
			else:
				CompType[complaintType] += 1
				
		for key, value in CompType.iteritems():
			print "%s with %s complaints" % (key, value)
			
openFile(csvFile)
