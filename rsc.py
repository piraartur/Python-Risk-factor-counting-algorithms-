import matplotlib.pyplot as mp
import plotly as pl
import csv
from datetime import datetime
import sys


def jump(lineno):
    frame = sys._getframe().f_back
    called_from = frame

    def hook(frame, event, arg):
        if event == 'line' and frame == called_from:
            try:
                frame.f_lineno = lineno
            except ValueError as e:
                print("jump failed:", e)
            while frame:
                frame.f_trace = None
                frame = frame.f_back
            return None
        return hook

    while frame:
        frame.f_trace = hook
        frame = frame.f_back
    sys.settrace(hook)


def analyze_csv(filename,a,b=0,c=1):
	'''Function analyzing csv file'''
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(f)
		#print(header_row)
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
	print("Please, be aware that it is beta version, all exceptions to bugs are not done yet;")
	print("However you can use it with 4 operations.")
	print("New releases will support french, italian and polish translations.")
	print("If you want to hear when update will be available, contact me on github (link below).")
	print("Please, specify what would you like to do with your data.")
	print("If you enjoy my simple calculator, please give star at https://github.com/piraartur")
	print("or recommend my tool to other people.")
	print("Thank you for using this tool. It means much to me.")
	print("PS. If you happen to encounter some bugs correlated strictly to math operations\n of this calculator contact me instantly")
	print("Author of this calculator is not accountable for risk management, decision making and investments\n of this app users.")
	print("Be aware that the author is not proffessional, does not provide proffessional services. \nThis app can be viewed only as an author python syntax exercise, not investment decision provider ")
	print("neither as a system to risk (bet) money according to its calculations.")
	print("\n[1] -- Plot a chart")
	print("[2] -- Calculate volatility")
	print("[3] -- Calculate Value at Risk (VaR)")
	print("[4] -- Calculate beta (you know your current asset gain and market gain")
	print("[N/A] -- AVAILABLE IN FUTURE (cVaR, Hedge Ratio))")
	print("[0] -- Quit")
	answer =  int(input())
	return answer

	

