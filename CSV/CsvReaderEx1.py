#Program for Reading the data from CSV File by using CSV Module
#CsvReaderEx1.py----csv.reader()---Gives an object csv.reader class object
import csv
try:
	with open("stud.csv","r") as fp:
		print("----------------------------------------------")
		csvr=csv.reader(fp) # here csvr is an object of  <class, _csv.reader>
		for record in csvr:
			for val in record:
				print("{}".format(val),end="\t")
			print()
		print("----------------------------------------------")
except FileNotFoundError:
	print("File does not exist")