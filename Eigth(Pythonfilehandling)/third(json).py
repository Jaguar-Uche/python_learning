
# Python Writing files (.txt, .json, .csv)

import json

employee ={
    "name":"Spongebob",
    "position":"cook",
    "age":30
}

filepath="files/employees.json"

try:
    with open(filepath, "x") as file:
        json.dump(employee,file, indent=4)
        # The dictionary to do and the file to create it to
        print(f"txt file '{filepath}' was created successfully")
except FileExistsError:
    with open(filepath, "a") as file:
        file.write(",\n")
        json.dump(employee,file,indent=4)
        # The dictionary to do and the file to create it to
        print(f"txt file '{filepath}' already exists")
