name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

print(f"{name} has {len(name)} characters")
#includes spaces

index = name.find("S")
location = "Not found" if index == -1 else f"Found at position {index}"
print(f"S was {location}")
#this returns the first occurrence of a character and -1 if the character does not exist(indexed from 0)


print(name.rfind("a"))
#The last occurrence of a character

print(name.capitalize())
#This capitalizes the first letter of the string(only the letter at position 0)

print(name.upper())
#This capitalizes all the characters in a string

print(name.lower())
#To make all the characters lowercase

only_digits = name.isdigit()
#returns true if your string contains only digits
print(only_digits)

only_letters = name.isalpha()
#returns true if your string contains only alphabetical characters(space and slashes are not alphabetical characters)
print(only_letters)

dashes = phone_number.count(" ")
#retuns the number of spaces in the string
print(dashes)

phone_number = phone_number.replace(" ", "-")
#replaces all occurrence of a string with a -
print(phone_number)

name = name.replace(" ", "")
#replaces spaces with nothing
print(name)

# print(help(str))
#methods operable on string

print("Username must not contain space or digits and must be shorter than 12")
user_name = input("Enter username: ")
valid_user_name = len(user_name) <=12 and user_name.isalpha()
if valid_user_name:
    print("Your username is valid")
else:
    print("Your username is not valid")

#indexing - locating elements of a string by their index

credit_card_number = "1234-4564-8757-2023"
print(credit_card_number)
print(credit_card_number[:2])

print(credit_card_number[0])
#the first letter
print(credit_card_number[0:5])
#start and then the number of characters before it stops(the end index but it does not include the character at th end index(exclusive))
#this prints the first four digits of our string
print(credit_card_number[:3])
#python assumes it is the beginning of the string u are starting from
print(credit_card_number[3:])
#python assumes u are starting from 3 and ending at the end
print(credit_card_number[-1])
#prints the last character in the string and in that order -2 for the second(compound interest) to the last and -3 for the third to the last
print(credit_card_number[::2])
#starts from 0 and prints second(compound interest) characters in that order
print(credit_card_number[1::2])
last_digits = credit_card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")



credit_card_number = credit_card_number[::-1]
#for reversing the order of strings
print(credit_card_number)

