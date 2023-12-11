import os

try:
    filename = str(input("Enter File Name : "))
    if os.path.exists(filename) and filename.endswith('.csv'):
        os.remove(filename)
        print("File Deleted")
except FileNotFoundError:
    print("File Not Found !")
