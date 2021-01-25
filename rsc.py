import matplotlib.pyplot as mp
import plotly as pl
import csv
from datetime import datetime
import numpy as np
import math
import PySimpleGUI as sg 

#User-interactive query for his data set
print("Please write the name of csv file with data you want to analyze.")

csv = input()
filename = f"{csv}.csv"

print("You have stated that your data")
print(f"is located in {filename}.")
print("Do you confirm? If you agree, type 'Yes'.")
print("If you don't agree and would like to")
print("input name of the file again, type 'No'.")

answer = input()
while answer != "Yes":
	print("Please input your filename once again.")
	csv = input()
	filename = f'{csv}.txt'
	print("You have stated that your data")
	print(f"is located in {filename}.")
	print("Do you confirm? If you agree, type 'Yes'.")
	answer_2 = input()
	if answer_2 == 'Yes':
		break
