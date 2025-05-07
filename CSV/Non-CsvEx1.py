#Program for Reading the data from CSV File by using File Pointer (Normal Files)
#Non-CsvEx1.py
try:
	with open("stud.csv","r") as fp:
		print("----------------------------------------------")
		filedata=fp.read()
		print(filedata)
		print("----------------------------------------------")
except FileNotFoundError:
	print("File does not exist")