import csv

try:
    filename = str(input("Enter File Name : "))
    with open(filename) as file:
        read = csv.reader(file, delimiter=',')
        print("%10s"%"Column1","%20s"%"Column2","%10s"%"Column3")
        print("====================================================")
        for row in read:
            print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2])
except FileNotFoundError:
    print("File Not Found !")

