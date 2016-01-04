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
		
		minDate = datetime.strptime("9999-12-31", "%Y-%m-%d")
		maxDate = datetime.strptime("0001-01-01", "%Y-%m-%d")
		
		for row in csvReader:
			num_complaints += 1
			uniqueKey = row[0]
			createDate = datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p')
			
			if createDate < minDate:
				minDate = createDate
			if createDate > maxDate:
				maxDate = createDate
			
							
		print '%s complaints between %s and %s' % (num_complaints, minDate.strftime('%m/%d/%Y %H:%M:%S'), maxDate.strftime('%m/%d/%Y %H:%M:%S'))

			
openFile(csvFile)
