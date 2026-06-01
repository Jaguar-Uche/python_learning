
# Multithreading - performing multiple tasks concurrently
# Used for I/O bound tasks like reading files or fetching data from APIS
# threading.Thread(target=my_function)

import threading
import time

def walk_dog(dog_name,walker_name):
    time.sleep(8)
    print(f"{walker_name} has finished walking {dog_name}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

walk_dog("Scooby","Nkechi")
take_out_trash()
get_mail()

# They are running on the same thread so they complete one by one

print("***********")

chore1 = threading.Thread(target=walk_dog, args=("Regan","Nkechi"))
# target = walk dog means walk dog is the first chore you have to do
# If the function accepts a parameter, pass in an args, which is a tuple(,), end with a comma
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)
chore1.start()
chore2.start()
chore3.start()
# Here you finish taking out the trash first because it is the smallest then you get the mail, then walk the dog
chore1.join()
chore2.join()
chore3.join()
# the .join() waits for the chores to finish before it executes the rest of the program
print("**********")
print("All Chores are complete")
# This is on the sam thread as the other codes so it runs after the first ones not after the threads have finished