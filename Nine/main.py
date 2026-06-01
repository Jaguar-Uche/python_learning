
# Date and time in python

import datetime

date = datetime.date(2020,1,3)
today = datetime.date.today()
time = datetime.time(12,30,0)
now = datetime.datetime.now()

print(date)
print(today)
print(time)
print(now)

now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

target_datetime = datetime.datetime(2020,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
