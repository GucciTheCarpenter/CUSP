# import pandas as pd
# from pandas import DataFrame, Series
# import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os
import sys

csvFile = sys.argv[1]

def openFile(filename):
	
	with open(filename) as f:
		csvReader = csv.reader(f)
		headers = next(csvReader)
		
		AgencyCount = {}
		AgencyReq1 = ['NYPD', 'TLC', 'DPR']
		AgencyPlot = {}
		
		for row in csvReader:
			uniqueKey = row[0]
			parseDate = row[1].split(' ')
			createDate = datetime.strptime(parseDate[0], '%m/%d/%Y')
			Agency = row[3]
			
			#print createDate.strftime('%m/%d/%Y')
			
			if not Agency in AgencyCount:
				AgencyCount[Agency] = {createDate: 1}
			if Agency in AgencyCount and not createDate in AgencyCount[Agency]:
				AgencyCount[Agency][createDate] = 1
			else:
				AgencyCount[Agency][createDate] += 1
			
				
		for key in AgencyCount:
			if key in AgencyReq1:
				AgencyPlot[key] = AgencyCount[key]
		
			
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
