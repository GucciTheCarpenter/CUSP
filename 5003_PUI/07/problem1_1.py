# import pandas as pd
# from pandas import DataFrame, Series
# import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys

csvFile = sys.argv[1]

def openFile(filename):
	
	with open(filename) as f:
		csvReader = csv.reader(f)
		headers = next(csvReader)
		
		AgencyCount = {}
		AgencyReq1 = ['NYPD', 'DOT', 'DOB', 'TLC', 'DPR']
		AgencyPlot = {}
		
		for row in csvReader:
			uniqueKey = row[0]
			Agency = row[3]
			
			if not Agency in AgencyCount:
				AgencyCount[Agency] = 1
			else:
				AgencyCount[Agency] += 1
				
		for key in AgencyCount:
			if key in AgencyReq1:
				AgencyPlot[key] = AgencyCount[key]
				
				
		plt.bar(range(len(AgencyPlot)), AgencyPlot.values(), align='center')
		plt.xticks(range(len(AgencyPlot)), AgencyPlot.keys())
		
		plt.ylabel('Complaint Counts')
		plt.xlabel('Agency')
		plt.show()
		
openFile(csvFile)
