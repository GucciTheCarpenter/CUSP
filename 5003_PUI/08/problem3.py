import os
import datetime
from datetime import datetime
import pandas as pd
import pandas.io.data
import matplotlib.pyplot as plt
import pylab
import sys

# csvFile = sys.argv[1]

def openFile(filename):
	
	df_mp = pd.read_csv(filename)
	
	df_year = df_mp[['Processor', 'Year of Introduction']].sort('Year of Introduction')
	df_year['x_axis'] = range(len(df_year))
	Proc_year = []
	for i in df_year['Processor']:
		Proc_year.append(i)
	
	df_trans = df_mp[['Processor', 'Transistors']].sort('Transistors')
	df_trans['x_axis'] = range(len(df_trans))
	
	fig, ax = plt.subplots(1, 2)
	
	
	ax[0].plot(df_year['x_axis'], df_year['Year of Introduction'], 'ro')
	ax[0].set_xticks(range(len(df_year['Processor'])))
	ax[0].set_xticklabels(df_year['Processor'], rotation='vertical')
	ax[0].set_title('Year of Introduction')
	ax[0].set_ylabel('Year')
	
	
	ax[1].plot(df_trans['x_axis'], df_trans['Transistors'], 'ro')
	# ax[1].set_xticks(df_trans['x_axis'], df_trans['Processor']) #, rotation='vertical')	
	ax[1].set_xticks(range(len(df_trans['Processor'])))
	ax[1].set_xticklabels(df_trans['Processor'], rotation='vertical')
	ax[1].set_yscale('log')
	ax[1].set_title('Number of Transistors')
	ax[1].set_ylabel('Transistors')
	
	plt.tight_layout()
	plt.show()


if __name__ == '__main__':
	
	openFile(sys.argv[1])
