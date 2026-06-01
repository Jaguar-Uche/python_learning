
# A Comma Separated value file

import csv

file_path = "files/employees.csv"

employees =[["Name", "Age", "Job"],
            ["Spongebob",30,"Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy",27,"Scientist"]]

with open(file_path, "w", newline="") as file:
        # csv sets new line after it writes. to prevent that, set newline =""
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        # writer is an object that provides methods for writing to a csv file
        print(f"csv file '{file_path}' was created")
