# import pandas as pd
# from pandas import DataFrame, Series
# import numpy as np
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
		zipCountAgency = {}
		zipTopAgency = {}
		AgencyReq1 = ['NYPD', 'DOT', 'DOB', 'TLC', 'DPR']
		AgencyColor = {'NYPD': 'b', 'DOT': 'r', 'DOB': 'g', 'TLC': 'y', 'DPR': 'm'}
		inv_AgencyColor = {v: k for k, v in AgencyColor.items()}
		inv_AgencyColor['w'] = 'N/A'
		
		for row in csvReader1:
			uniqueKey = row[0]
			Agency = row[3]
			zipCode1 = row[8]
			
			if len(str(zipCode1)) == 5 and int(zipCode1) > 0 and int(zipCode1) < 100000:
				if not zipCode1 in zipCount:
					zipCount[zipCode1] = 1
				else:
					zipCount[zipCode1] += 1
					
			if Agency in AgencyReq1:
				if not zipCode1 in zipCountAgency:
					zipCountAgency[zipCode1] = {Agency: 1}
				if zipCode1 in zipCountAgency and not Agency in zipCountAgency[zipCode1]:
					zipCountAgency[zipCode1][Agency] = 1
				else:
					zipCountAgency[zipCode1][Agency] += 1
					
		for key in zipCountAgency:
			zipSortAgency = sorted(zipCountAgency[key].items(), key=lambda x: (-x[1]))
			zipTopAgency[key] = zipSortAgency[0][0]
			
		# print zipTopAgency					
		
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
			Z = []
			T = []
			
			for key in zipPop:
				if key in zipCount and zipTopAgency:
					X.append(zipPop[key])
					Y.append(zipCount[key])
					Z.append(key)
					T.append('w')

					
			for n,i in enumerate(Z):
				if i in zipTopAgency:
					T[n] = AgencyColor[zipTopAgency[i]]
					
	
			plt.scatter(X, Y, c=T)
			plt.ylabel('Complaint Counts')
			plt.xlabel('Zip Population')
	

			plt.show()
					
		
openFile(csvFile1, csvFile2)
