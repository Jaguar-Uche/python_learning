#for loop

#the range is exclusive so u begin at 1 and stop once u reach 11.
#the third one is the step
for x in range(1,11,2):
    print(x)

print("Happy New Year! ")

#This makes the range first before reversing it so it starts from 9
#because it incremented from 1 to 10 in 2 step before reversing
for x in reversed(range(1,11,2)):
    print(f"number {x}")
print("I am done with the reversed for loop")

credit_card = "1234-5678-9012-3456"

# for x in range(0, len(credit_card)):
#     print(credit_card[x])

#This does this in a better way

for x in credit_card:
    print(x)
#prints the letters(x acts as the string at the index itself)

for x in range(1,21):
    if x == 13:
        continue
    elif x == 18:
        break
    else:
        print(x)
