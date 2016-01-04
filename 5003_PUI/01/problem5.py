import csv
import os
import datetime
from datetime import datetime
import sys

csvFile = sys.argv[1]

def openFile(filename):
	with open(filename) as f:
		csvReader = csv.reader(f)
		headers = next(csvReader)
		
		num_complaints = 0
		
		dayCount = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}
		dayOrder = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}

		
		for row in csvReader:
			
			uniqueKey = row[0]
			createDate = datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p')
			
			weekDay = createDate.strftime('%A')
			
			if weekDay in dayCount:
				dayCount[weekDay] += 1
				
		dayCountSorted = sorted(dayCount,key=dayOrder.get)
		
		for i in dayCountSorted:
			print i + ' == ' + str(dayCount[i])
			
		
		
openFile(csvFile)
