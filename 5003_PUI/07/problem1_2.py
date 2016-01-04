# import pandas as pd
# from pandas import DataFrame, Series
# numpy as np
import matplotlib.pyplot as plt
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
		# AgencyReq1 = ['NYPD', 'DOT', 'DOB', 'TLC', 'DPR']
		AgencyPlot = {}
		
		for row in csvReader:
			uniqueKey = row[0]
			Agency = row[3]
			
			if not Agency in AgencyCount:
				AgencyCount[Agency] = 1
			else:
				AgencyCount[Agency] += 1
				
		Agency_Sort =  sorted(AgencyCount.items(), key=lambda x: (-x[1], x[0]))
		
		Agency_Slice = Agency_Sort[:topK]
		
		for k,v in Agency_Slice:
			AgencyPlot[k] = v
		
		# print AgencyPlot
				
		plt.bar(range(len(AgencyPlot)), AgencyPlot.values(), align='center')
		plt.xticks(range(len(AgencyPlot)), AgencyPlot.keys())
		
		plt.ylabel('Complaint Counts')
		plt.xlabel('Agency')
		plt.show()
		
openFile(csvFile)
