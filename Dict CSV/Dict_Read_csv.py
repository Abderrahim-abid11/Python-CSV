import csv

class Csv:
    @classmethod
    def read_csv(cls, filename):
        with open(filename, newline='') as file:
            reade = csv.DictReader(file)
            items = list(reade)
            for row in items:
                print(row)

filename = str(input("Enter File Name : "))
Csv.read_csv(filename)

