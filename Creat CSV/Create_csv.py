import csv

filename = str(input("Enter File Name : "))
with open(filename, mode="w") as file:
    write = csv.writer(file, delimiter=',')
    print("File Create ...")
