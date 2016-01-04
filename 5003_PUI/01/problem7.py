import csv
import os
from collections import Counter
import sys

csvFile1 = sys.argv[1]
csvFile2 = sys.argv[2]

def openFile(filename1, filename2):
	with open(filename1) as f1:
		csvReader1 = csv.reader(f1)
		headers1 = next(csvReader1)
		
		zipComp = []
		
		for row in csvReader1:
			uniqueKey = row[0]
			complaintType = row[5]
			zipCode = row[7]
			
			zipComp.append(zipCode)
		
		# print zipComp, len(zipComp)
			
			
	with open(filename2) as f2:
		csvReader2 = csv.reader(f2)
		headers2 = next(csvReader2)
		
		zipBorough = {}
		BoroughComp = []
		
		for row in csvReader2:
			IncZip = row[0]
			Borough = row[1]
			
			if not IncZip in zipBorough:
				zipBorough[IncZip] = Borough
				
		for i in zipComp:
			BoroughComp.append(zipBorough[i])
			
		BoroughCount = Counter(BoroughComp).most_common()
		for k,v in BoroughCount:
			print (k.lower()).title() + ' with %s complaints' % (v)
			
		
			
openFile(csvFile1, csvFile2)
