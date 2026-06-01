import os
txt_data ="I like yam!"
txt_data2 = "Nkechi is a goat"

file_path ="output.txt"
file_path2 = "files/output.txt"
file_path3 = "C:\\Users\\Alex\\Desktop\\output.txt"
employee_file_path ="employee.txt"

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

with open(file_path2, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path2}' was written to")

try:
    with open(file_path, "x") as file:
        file.write(txt_data2)
        print(f"txt file '{file_path}' was created and written to")
except FileExistsError:
    with open(file_path, "a") as file:
        file.write("\n" + "I am a big boy")
        print(f"txt file '{file_path}' was appended to")
# With closes the file when we are done with it
# open() returns a file object, the first param is file path, second is mode.
# w is for write and
# x writes too if the file doesn't exist
# a is for appending
# r is for reading
# as file means the name is file

if os.path.exists(employee_file_path):
    with open(employee_file_path, "a") as file:
        for employee in employees:
            file.write(employee + "\n")
else:
    with open(employee_file_path, "a") as file:
        for employee in employees:
            file.write(employee + "\n")