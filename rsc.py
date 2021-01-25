import matplotlib.pyplot as mp
import plotly as pl
import csv
from datetime import datetime
import numpy as np
import math
import PySimpleGUI as sg 

#User-interactive query for his data set
print("Please write the name of csv file with data you want to analyze.")

data = input()
filename = f"{data}.csv"

print("You have stated that your data")
print(f"is located in {filename}.")
print("Do you confirm? If you agree, type 'Yes'.")
print("If you don't agree and would like to")
print("input name of the file again, type 'No'.")

answer = input().upper()
while answer != "YES":
	print("\nPlease input your filename once again.")
	data = input()
	filename = f'{data}.csv'
	print("You have stated that your data")
	print(f"is located in {filename}.")
	print("\nDo you confirm? If you agree, type 'Yes'.")
	answer_2 = input().upper()
	if answer_2 == 'YES':
		break

#Now code for user-interactive decision on how to analyze data
print("Welcome to @piraartur risk calculator.")
print("Please, specify what would you like to do with your data.")
print("\n[1] -- Plot a chart")
print("[2] -- Calculate volatility")
print("[3] -- Calculate Value at Risk (VaR)")
print("[4] -- Calculate beta (you know your current asset gain and market gain")
print("[5] -- Calculate model beta (you don't know asset gain or market gain - or both)")
print("[6] -- Quit")

i = 0
while i !=20:
	print("#", end='')
	i += 1
print("\nTo specify what operation you would like to perform, type number with numpad.")
i = 0
while i !=20:
	print("#", end='')
	i += 1


answer = int(input())
if answer == 1:
	print("Please type name of your chart, or leave it blank.")
	name_of_asset = input()
	print("Please state in which column there are values for price highs BY ENTEING NUMBER.")
	a = int(input())
	print("Please state in which column there are date values BY ENTERING NUMBER.")
	b = int(input())
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
	fig, ax = mp.subplots()
	ax.plot(dates, highs, c='black')
	ax.set_title(f" {name_of_asset} ", fontsize=14)
	ax.set_ylabel("Price")
	ax.set_xlabel("Date")
	fig.autofmt_xdate()
	ax.tick_params(axis='both', which='major', labelsize=14)
	mp.show()

if answer == 2:
	print("Please state in which column there are values for price highs BY ENTERING NUMBER.")
	a = int(input())
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(f)
		highs = []
		for row in reader:
			high = float(row[a])
			highs.append(high)
	mean = sum(highs)/len(highs)
	crrt_price = highs[0]
	variances = []
	for high in highs:
		variances.append(mean-high)
	ttps =[]
	for variance in variances:
		
		ttp = variance*variance
		ttps.append(ttp)
	ttp_avg = sum(ttps)/len(ttps)
	volatility = math.sqrt(ttp_avg)	
	print(f"Calcuated value of volatility equals {volatility}")
