import datetime
import pandas as pd
import pandas.io.data
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import os, sys

def openFile(filename):
	
	df_stocks = pd.read_csv(filename, index_col=0)
	df_stocks_asc = df_stocks.sort_index(ascending=True)
	
	ts_AAPL = df_stocks_asc['apple']
	ts_MSFT = df_stocks_asc['microsoft']
	
	df_stocks_asc['AAPL_base'] = df_stocks_asc['apple']/df_stocks_asc['apple'][0]
	df_stocks_asc['MSFT_base'] = df_stocks_asc['microsoft']/df_stocks_asc['microsoft'][0]
	
	ts_AAPL_base = df_stocks_asc['AAPL_base']
	ts_MSFT_base = df_stocks_asc['MSFT_base']
	# print ts_AAPL_base.iloc
	
	# xticks_1 = 
	#xticks_0 = pylab.setp(axs[0], xticklabels=(ts_AAPL_base.index))
	
	fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
	axs[0].plot(ts_AAPL_base)
	axs[0].set_xlabel('month')
	axs[0].set_ylabel('Indexed Return')
	axs[0].set_title('AAPL')
	axs[0].grid(True, which='both')
	# axs[0].set_xticklabels(ts_AAPL_base.index, rotation='vertical')
	
	axs[1].plot(ts_MSFT_base, c='g')
	axs[1].set_xlabel('month')
	axs[1].set_ylabel('Indexed Return')
	axs[1].set_title('MSFT')
	axs[1].grid(True, which='both')
	# axs[1].set_xticklabels(ts_MSFT_base.index, rotation='vertical')
	
	plt.show()
	



if __name__ == '__main__':
	
	openFile(sys.argv[1])
