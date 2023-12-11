import os
import shutil

try:
    filename = str(input("Enter File Name : "))
    newfile = str(input("Enter New File : "))
    if os.path.exists(filename) and filename.endswith('.csv'):
        shutil.copy2(filename, newfile)
        print("Content Copyed ... !")
except FileNotFoundError:
    print("File Not Found .")
