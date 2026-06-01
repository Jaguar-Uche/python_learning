
# Python reading files

import json
import csv

file_path = "files/output.txt"
file_path2 = "files/nopermission.txt"
file_path3 = "files/employees.json"
file_path4 = "files/employees.csv"

try:
    with open(file_path,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found.")

try:
    with open(file_path2,"r") as file:
        content = file.read()
        print(content)
except PermissionError:
    print("You don't have permission to read this file.")

try:
    with(open(file_path3,"r")) as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("File not found.")

try:
    with(open(file_path4, "r")) as file:
        content = csv.reader(file)
        print(content)
        # THis prints a memory address
        for line in content:
            print(line)
        print(line[1])
except FileNotFoundError:
    print("File not found.")

