import csv

try:
    filename = input("Enter File Name: ")
    add = 'Y'
    while add.upper() == 'Y':
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            rows = list(reader)

        found = False
        row_id = int(input("Enter Row Id Number: "))
        row_update = int(input("Update Row (1/2): "))
        update = input("Enter New Value: ")

        for row in rows:
            if len(row) != 0 and int(row[0]) == row_id:
                row[row_update] = update
                print("=====================")
                print(f"Id Number: {row[0]}")
                print(f"Id Name  : {row[1]}")
                print(f"Id Age   : {row[2]}")
                print("=====================")
                found = True
                break

        if not found:
            print("==============")
            print("Id Not Found")
            print("==============")
        else:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        add = input("For More Enter (Y) OR (Q) For Quit: ")
        if add.upper() == 'Q':
            add = 'Q'

except FileNotFoundError:
    print("File Not Found!")

