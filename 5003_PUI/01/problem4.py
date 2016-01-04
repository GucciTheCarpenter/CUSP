import csv
import os
import sys

csvFile = sys.argv[1]
topK = int(sys.argv[2])

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
		
		CompList = []
		
		for item, number in CompType_Sort:
			CompList.append("%s with %s complaints" % (item, number))
		
		# topK = 3
			
		CompList_Slice = CompList[0:topK]
		
		for i in CompList_Slice:
			print i
				
			
openFile('sample_data_problem_4.csv')
