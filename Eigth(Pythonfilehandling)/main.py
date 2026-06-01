
import os
# A way for python programs to interact with the operating system

file_path = "files/test.txt"
file_path2 = "C:/Users/Alex/Desktop/codes/learning/python/pythonProject/Eigth(Pythonfilehandling)"
# We could use either a relative file path(folder/test.txt)
# or an absolute file path(C:/Users/Alex/Desktop/codes/learning/python/pythonProject/Eigth(Pythonfilehandling)/test.txt)

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
else:
    print(f"That location doesn't exist")

if os.path.exists(file_path2):
    print(f"The location '{file_path2}' exists")
    if os.path.isfile(file_path2):
        print("That is a file")
    elif os.path.isdir(file_path2):
        print("That is a directory")
else:
    print(f"That location doesn't exist")