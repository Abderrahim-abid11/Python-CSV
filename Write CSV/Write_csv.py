import os
import csv

try:
    filename = str(input("Enter File Name : "))
    with open(filename, mode='w') as file:
        write = csv.writer(file, delimiter=',')
        add = 'Y'
        while add.upper() == 'Y':
            column1 = int(input("Enter Id Number : "))
            column2 = str(input("Enter Id  Name : "))
            column3 = int(input("Enter Id Age : "))
            write.writerow([column1,column2,column3])
            print("$$$ Data Save ... $$$")
            add = str(input("For Add More (Y) OR (Q) For Quit : "))
            if add.upper() == 'Q':
               add = 'Q'
except FileNotFoundError:
    print("File Not Found !")
