import time

timer = int(input("Enter the time in seconds: "))
for x in range(0,timer):
    print(x)
    time.sleep(1)

#time.sleep(3)
#makes the program sleep for 3 seconds. after 3 seconds, print something

print("Hello, i am awake now!")

timer = int(input("Enter the time in seconds: "))

for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("I am done with you, now get away! ")