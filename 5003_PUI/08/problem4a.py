import csv
import os
import datetime
from datetime import datetime
import pandas as pd
import pandas.io.data
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import sys

# csvFile = sys.argv[1]

def openFile(filename):
	
	df_genes = pd.read_csv(filename)
	df_genes2 = df_genes[['A', 'C', 'D', 'B']]
	
	# print df_genes2.head()
	# plt.show()
	gene_scatter = pd.scatter_matrix(df_genes2)
	gene_scatter
	plt.show()
	
	
if __name__ == '__main__':
	
	openFile(sys.argv[1])
