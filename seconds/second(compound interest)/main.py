#Compound Interest

principal = 0
rate = 0
time = 0


while True:
    principal = float(input("Enter the principal amount: "))
    if principal <0:
        print("Principal cannot be less than 0")
    else:
        break
#while true makes it continue until the break function inside is encountered

#if you use <0, it would only enter while loop if it is less than zero and u initialized to be 0 so it never enters while loop
while rate <=0:
    rate = float(input("Enter the interest rate: "))
    if rate <=0:
        print("rate cannot be less than or equal to 0")

while time <=0:
    time = int(input("Enter the time(years): "))
    if time <=0:
        print("Time cannot be less than or equal to 0")

total = principal* pow((1 + rate/100), time)

print(f"Your amount after {time} years is #{total: .2f}")