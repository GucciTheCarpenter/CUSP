import csv
import os
import datetime
from datetime import datetime
import sys
import collections
import matplotlib.pyplot as plt


csvFile = sys.argv[1]

def openFile(filename):
	with open(filename) as f:
		csvReader = csv.reader(f)
		headers = next(csvReader)
		
		ts_list = []
		ts_dict = {}
		
		for row in f:
			row_strip = row.strip()
			ts_list.append(datetime.strptime(row_strip, '%Y-%m-%d %H:%M:%S'))
		
		# number of bins	
		ts_bins = int(len(ts_list) ** .5)
		
		# width of bins
		ts_step = (max(ts_list) - min(ts_list))/ts_bins
		
		# initiate dict with bin cut-offs
		for i in range(ts_bins + 1):
			ts_dict[min(ts_list) + (ts_step * i)] = 0
		
		# set a time floor / datetime.timedelta(0)	
		ts_zero = min(ts_list) - min(ts_list)
		
		# set instance counts in dict
		for i in ts_list:
			for k in ts_dict:
				if k - i >= ts_zero and k - i <= ts_step:
					ts_dict[k] += 1	
		
		# assignment dates
		assign_dates = ['2007-09-18 12:00:00', '2007-09-18 12:00:00', '2007-10-04 12:00:00',
		'2007-10-25 12:00:00', '2007-11-27 12:00:00', '2007-12-15 12:00:00', '2007-12-11 12:00:00']
		assign_dict = {}
		
		for i in assign_dates:
			assign_dict[datetime.strptime(i, '%Y-%m-%d %H:%M:%S')] = 7000
			
		# print assign_dict
		ts_dict.update(assign_dict)
			
		
		# chronological dict
		ts_dict_ord = collections.OrderedDict(sorted(ts_dict.items()))
		
		
		# print ts_list[:3], ts_bins, ts_step
		# print ts_dict_ord, len(ts_dict_ord)
		
		plt.bar(range(len(ts_dict_ord)), ts_dict_ord.values(), align='center')
		# plt.xticks(range(len(ts_dict_ord)), ts_dict_ord.keys(), rotation='vertical')
		
		plt.title('Scientific Visualization Course')
		plt.ylabel('timestamps')
		plt.xlabel('date')
		
		plt.show()
		
		
		
		


openFile(csvFile)
