#Program for adding Record to  CSV File by Python Program with csv module
#CsvWriteEx3.py-----csv.writer()  gives an object of <class, _csv.Writer>
import csv  # Step-1
with open("emp.csv","a") as fp:
	while(True):
		print("----------------------------------------------------")
		#accept the employee values from KBD
		eno=int(input("Enter Employee Number:"))
		ename=input("Enter Employee Name:")
		sal=float(input("Enter  Employee Salary:"))
		dsg=input("Enter Employee Desgination:")
		#create an empty list
		lst=list()
		#append employee Data to list object
		lst.append(eno)
		lst.append(ename)
		lst.append(sal)
		lst.append(dsg)
		#create an object ccsv.Writer object
		csvwr=csv.writer(fp)
		#write  record data to csv file---writerow()
		csvwr.writerow(lst)
		print("Recod Saved in a File:")
		print("----------------------------------------------------")
		ch=input("Do u want to insert another Record(yes/no):")
		if(ch.lower()=="no"):
			break
		

