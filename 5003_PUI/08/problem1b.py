import datetime
import pandas as pd
import pandas.io.data
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl
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
	
	ts_AAPL_base.plot(label='Apple')
	ts_MSFT_base.plot(label='Microsoft')
	plt.title('AAPL v. MSFT')
	plt.ylabel('Indexed Return')
	plt.legend(loc='best')
	
	plt.show()
	



if __name__ == '__main__':
	
	openFile(sys.argv[1])
