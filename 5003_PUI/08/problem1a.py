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
	
	ts_AAPL.plot(label='Apple')
	ts_MSFT.plot(label='Microsoft')
	plt.title('AAPL v. MSFT')
	plt.ylabel('Price ($)')
	
	plt.legend(loc='best')
	
	plt.show()
	



if __name__ == '__main__':
	
	openFile(sys.argv[1])
