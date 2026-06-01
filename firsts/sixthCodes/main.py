#logical operators
temp = -5
is_raining = False
is_sunny = True
if temp > 35 or temp <0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is hot outside😒")
    print("It is sunny")

elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temp >0 and is_sunny:
    print("It is warm outside")
    #temp <28 and temp >0 is the same as 28> temp>0
    print("It is sunny")
elif not is_sunny:
    print("It is cloudy")


#conditional expression(ternary operator)
num = -6
a = 6
b = 2
age = 2
temperature = 30
user_role = "admin"
print("Positive" if num>0 else "Negative")
print("Even" if num%2==0 else "Odd")

max_num = a if a>b else b
print(max_num)
min_num = a if a<b else b
print(min_num)

status = "Adult" if age>=18 else "Child"
weather = "Hot" if temperature>20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(status)
print(weather)
print(access_level)