
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os
import sys

csvFile1 = sys.argv[1]
csvFile2 = sys.argv[2]

def openFile(filename1, filename2):
	
	with open(filename1) as f1:
		csvReader1 = csv.reader(f1)
		headers1 = next(csvReader1)
		
		zipCount = {}
		# AgencyCountAgr = {}
		# AgencyReq1 = ['NYPD', 'TLC', 'DPR']
		AgencyPlot = {}
		
		for row in csvReader1:
			uniqueKey = row[0]
			Agency = row[3]
			zipCode1 = row[8]
			
			if len(str(zipCode1)) == 5 and int(zipCode1) > 0 and int(zipCode1) < 100000:
				if not zipCode1 in zipCount:
					zipCount[zipCode1] = 1
				else:
					zipCount[zipCode1] += 1
					
		
		with open(filename2) as f2:
			csvReader2 = csv.reader(f2)
			headers2 = next(csvReader2)
			
			zipPop = {}
			
			for row in csvReader2:
				zipCode2 = row[0]
				Pop = row[1]
				
				if not zipCode2 in zipPop:
					zipPop[zipCode2] = Pop
					
			X = []
			Y = []
			
			for key in zipPop:
				if key in zipCount:
					X.append(zipPop[key])
					Y.append(zipCount[key])
					
			
			plt.scatter(X, Y)
			plt.ylabel('Complaint Counts')
			plt.xlabel('Zip Population')
			plt.show()
					
		
openFile(csvFile1, csvFile2)
