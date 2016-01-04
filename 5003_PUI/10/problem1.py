import os, sys
import csv
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt


def getTimeSeries(filename):
	df_311 = pd.read_csv(csvFile, parse_dates='Created Date')
	boro_df = df_311[['Created Date', 'Borough']]
	
	return boro_df
	
def getComplaints(boroTimeSeries):
	indexed_boro_df = boroTimeSeries.set_index(pd.to_datetime(boroTimeSeries['Created Date']))
	indexed_boro_df['Complaint Count'] = 1
	indexed_boro_df = indexed_boro_df.drop('Created Date', 1)
	
	return indexed_boro_df
	
def getDataFrame(boroComplaints):
	bx_df = pd.DataFrame(boroComplaints[boroComplaints['Borough'] == 'BRONX']['Complaint Count'])
	bx_df.rename(columns={'Complaint Count': 'BRONX'}, inplace=True)
	bx_df = bx_df.resample('D', how='sum')
	
	bk_df = pd.DataFrame(boroComplaints[boroComplaints['Borough'] == 'BROOKLYN']['Complaint Count'])
	bk_df.rename(columns={'Complaint Count': 'BROOKLYN'}, inplace=True)
	bk_df = bk_df.resample('D', how='sum')
	
	mh_df = pd.DataFrame(boroComplaints[boroComplaints['Borough'] == 'MANHATTAN']['Complaint Count'])
	mh_df.rename(columns={'Complaint Count': 'MANHATTAN'}, inplace=True)
	mh_df = mh_df.resample('D', how='sum')
	
	qu_df = pd.DataFrame(boroComplaints[boroComplaints['Borough'] == 'QUEENS']['Complaint Count'])
	qu_df.rename(columns={'Complaint Count': 'QUEENS'}, inplace=True)
	qu_df = qu_df.resample('D', how='sum')
	
	si_df = pd.DataFrame(boroComplaints[boroComplaints['Borough'] == 'STATEN ISLAND']['Complaint Count'])
	si_df.rename(columns={'Complaint Count': 'STATEN ISLAND'}, inplace=True)
	si_df = si_df.resample('D', how='sum')
	
	bxbk_df = bx_df.join(bk_df, how='outer')
	mhqu_df = mh_df.join(qu_df, how='outer')
	four_df = bxbk_df.join(mhqu_df, how='outer')
	
	return four_df.join(si_df, how='outer')
	
# def createPlot(boroDataFrame):
# 	boroDataFrame.resample('5min', how='sum').plot()
	
	

'''	
def getDataFrame(boroTimeSeries):
	bx_dict = {}
	bk_dict = {}
	mh_dict = {}
	qu_dict = {}
	si_dict = {}
	
	for i in range(len(boroTimeSeries['boro_list'])):
		if boroTimeSeries['boro_list'][i] == 'BRONX':
			if not bx_dict[boroTimeSeries['date_list'][i]] in bx_dict:
				bx_dict[boroTimeSeries['date_list'][i]] = 1
			else: 
				bx_dict[boroTimeSeries['date_list'][i]] += 1
				
		if boroTimeSeries['boro_list'][i] == 'BROOKLYN':
			if bk_dict[boroTimeSeries['date_list'][i]] in bx_dict:
				bk_dict[boroTimeSeries['date_list'][i]] += 1
			else: 
				bk_dict[boroTimeSeries['date_list'][i]] = 1
			
		if boroTimeSeries['boro_list'][i] == 'MANHATTAN':
			if mh_dict[boroTimeSeries['date_list'][i]] in bx_dict:
				mh_dict[boroTimeSeries['date_list'][i]] += 1
			else: 
				mh_dict[boroTimeSeries['date_list'][i]] = 1
			
		if boroTimeSeries['boro_list'][i] == 'QUEENS':
			if qu_dict[boroTimeSeries['date_list'][i]] in bx_dict:
				qu_dict[boroTimeSeries['date_list'][i]] += 1
			else: 
				qu_dict[boroTimeSeries['date_list'][i]] = 1
			
		if boroTimeSeries['boro_list'][i] == 'STATEN ISLAND':
			if si_dict[boroTimeSeries['date_list'][i]] in bx_dict:
				si_dict[boroTimeSeries['date_list'][i]] = 1
			else: 
				si_dict[boroTimeSeries['date_list'][i]] = 1
			
			
	return len(bx_dict), len(bk_dict), len(mh_dict), len(qu_dict), len(si_dict)

df_311 = pd.read_csv(csvFile, parse_dates='Created Date')

boro_df = df_311[['Created Date', 'Borough']]
indexed_boro_df = boro_df.set_index(pd.to_datetime(boro_df['Created Date']))
indexed_boro_df['Complaint Count'] = 1
indexed_boro_df = indexed_boro_df.drop('Created Date', 1)

bx_df = pd.DataFrame(indexed_boro_df[indexed_boro_df['Borough'] == 'BRONX']['Complaint Count'])
bx_df.rename(columns={'Complaint Count': 'BRONX'}, inplace=True)

bk_df = pd.DataFrame(indexed_boro_df[indexed_boro_df['Borough'] == 'BROOKLYN']['Complaint Count'])
bk_df.rename(columns={'Complaint Count': 'BROOKLYN'}, inplace=True)

boro_merge2 = bx_df.join(bk_df)'''



if __name__ == '__main__':
	csvFile = sys.argv[1]
	boroTimeSeries = getTimeSeries(csvFile)
	boroComplaints = getComplaints(boroTimeSeries)
	
	boroDataFrame = getDataFrame(boroComplaints)
	
	boroDataFrame.plot(figsize=(15,5))
	
	plt.title('Complaints over time')
	plt.show()



