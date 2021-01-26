import matplotlib.pyplot as mp
import plotly as pl
import csv
from datetime import datetime



def analyze_csv(filename,a,b=0,c=1):
	'''Function analyzing csv file'''
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(f)
		print(header_row)
		highs = []
		dates = []
		lows = []
		daily_returns=[]
		for row in reader:
			date = datetime.strptime(row[b], '%Y-%m-%d')
			high = float(row[a])
			highs.append(high)
			dates.append(date)
			low = float(row[c])
			lows.append(low)
			daily_return = ((low-high/low)*100)
			daily_returns.append(daily_return)
	mean = sum(highs)/len(highs)
	crrt_price = highs[-1]
	
	return dates, highs, mean, lows, daily_returns


def decoration():
	'''Line created to separate buttons'''
	i = 0
	while i !=20:
		print("#", end='')
		i += 1
	i = 0
	while i !=20:
		print("#", end='')
		i += 1
	print('\n')

def menu():
	'''Function showing menu panel'''
	#Now code for user-interactive decision on how to analyze data
	print("Welcome to @piraartur risk calculator.")
	print("Please, specify what would you like to do with your data.")
	print("\n[1] -- Plot a chart")
	print("[2] -- Calculate volatility")
	print("[3] -- Calculate Value at Risk (VaR)")
	print("[4] -- Calculate beta (you know your current asset gain and market gain")
	print("[5] -- Calculate model beta (you don't know asset gain or market gain - or both)")
	print("[6] -- Quit")
	answer =  int(input())
	return answer
	

