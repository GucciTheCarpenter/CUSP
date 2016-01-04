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
				
		CompType_Sort =  sorted(CompType.items(), key=lambda x: (-x[1], x[0]))
		
		for item, number in CompType_Sort:
			print "%s with %s complaints" % (item, number)
				
		# list1, list2 = zip(*CompType_Sort)
		# print list1, len(list1)
		# print list2
		
		# for i in list1:
		#	print str(i) + ' with ... complaints'
		
			
openFile(csvFile)
