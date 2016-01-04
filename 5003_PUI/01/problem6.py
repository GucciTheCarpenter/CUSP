import csv
import os
import collections
from collections import Counter
import sys

csvFile = sys.argv[1]

def openFile(filename):
	with open(filename) as f:
		csvReader = csv.reader(f)
		headers = next(csvReader)
		
		agencyComp = {}
		
		for row in csvReader:
			uniqueKey = row[0]
			agency = row[3]
			# complaintType = row[5]
			zipCode = row[7]
			
			if len(str(zipCode)) == 5 and int(zipCode) > 0 and int(zipCode) < 100000:
				if not agency in agencyComp:
					agencyComp[agency] = [zipCode]
				else:
					agencyComp[agency].append(zipCode)
		
		agencyComp_Ord = collections.OrderedDict(sorted(agencyComp.items()))
		
		
		for key in agencyComp_Ord:
			zipCount = 0
			topZips = []
			for i in agencyComp_Ord[key]:
				temp_zipCount = agencyComp_Ord[key].count(i)
				if temp_zipCount == zipCount:
					topZips.append(i)
				if temp_zipCount > zipCount:
					zipCount = temp_zipCount
					topZips = []
					topZips.append(i)
					
			unique_topZips = sorted(list(set(topZips)))
			
			print key, ' '.join([str(item) for item in unique_topZips]), zipCount
		
openFile(csvFile)
