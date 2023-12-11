import csv

try:
    filename = str(input("Enter File Name : "))
    add = 'Y'
    while add.upper() == 'Y':
        with open(filename, newline='') as file:
            reade = csv.reader(file, delimiter=',')
            found = False
            row_id = int(input("Enter Row Id Number : "))
            for row in reade:
                if len(row) != 0:
                    if int(row[0]) == row_id:
                        print("=====================")
                        print(f"Id Number : {row[0]}")
                        print(f"Id Name : {row[1]}")
                        print(f"Id Age : {row[2]}")
                        print("=====================")
                        found = True
                        break
            if not found:
                print("==============")
                print(" Id Not Found ")
                print("==============")
        add = str(input("For More Enter (Y) OR (Q) For Quit : "))
        if add.upper() == 'Q':
            add = 'Q'
except FileNotFoundError:
    print("File Not Found !")

