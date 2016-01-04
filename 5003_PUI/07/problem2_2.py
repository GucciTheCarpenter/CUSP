
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os
import sys

csvFile = sys.argv[1]
topK = int(sys.argv[2])

def openFile(filename):
	
	with open(filename) as f:
		csvReader = csv.reader(f)
		headers = next(csvReader)
		
		AgencyCount = {}
		AgencyCountAgr = {}
		# AgencyReq1 = ['NYPD', 'TLC', 'DPR']
		AgencyPlot = {}
		
		for row in csvReader:
			uniqueKey = row[0]
			parseDate = row[1].split(' ')
			createDate = datetime.strptime(parseDate[0], '%m/%d/%Y')
			Agency = row[3]
			
			#print createDate.strftime('%m/%d/%Y')
			
			if not Agency in AgencyCount:
				AgencyCount[Agency] = {createDate: 1}
				AgencyCountAgr[Agency] = 1
			if Agency in AgencyCount and not createDate in AgencyCount[Agency]:
				AgencyCount[Agency][createDate] = 1
				AgencyCountAgr[Agency] += 1
			else:
				AgencyCount[Agency][createDate] += 1
				AgencyCountAgr[Agency] += 1
			
				
		Agency_Sort =  sorted(AgencyCountAgr.items(), key=lambda x: (-x[1], x[0]))
		Agency_Slice = Agency_Sort[:topK]
		
		for i in Agency_Slice:
			if i[0] in AgencyCount:
				AgencyPlot[i[0]] = AgencyCount[i[0]]	
					
		for key in AgencyPlot:
			calls_sorted = sorted(AgencyPlot[key].items(), key=lambda x: (x[0]))
			dates, values = zip(*calls_sorted)
			# print dates, values
			plt.plot(dates, values, label=key)
		plt.ylabel('Complaint Counts')
		plt.xlabel('Date')
		plt.legend(loc='best')
		plt.show()
		
openFile(csvFile)
