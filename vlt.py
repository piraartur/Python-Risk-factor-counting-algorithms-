import matplotlib.pyplot as mp
import plotly as pl
import csv
from datetime import datetime



def analyze_csv(filename,a,b=0):
	'''Function analyzing csv file'''
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(f)
		print(header_row)
		highs = []
		dates = []
		for row in reader:
			date = datetime.strptime(row[b], '%Y-%m-%d')
			high = float(row[a])
			highs.append(high)
			dates.append(date)
	mean = sum(highs)/len(highs)
	crrt_price = highs[0]
	return dates, highs, mean