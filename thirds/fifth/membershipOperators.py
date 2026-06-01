# in , not in - whether a value or variable is found in a sequence(string, list, tuples, set or dictionary)

word = "APPLE"

letter = input("Guess a letter in the secret word:")
if letter.upper() in word:
    print(f"There is a/an {letter}")
else:
    print(f"{letter} not found")

if letter.upper() not in word:
    print("Heii you have guessed nonsense")
else:
    print("Spot on, you have guessed correctly")

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")
if student in students:
    print(f"{student} is a student of britarch")
else:
    print(f"{student} was not found")

grades = {"Sandy": "A",
          "Squidward":"B",
          "Spongebob":"C",
          "Patrick":"D"}
student = input("Enter the name of a student: ")
if student not in grades:
    print(f"{student} was not found")
else:
    print(f"{student}'s grade is {grades[student]}")

email = "alexuduma50@gmail.com"
if "@" in email and "." in email:
    print(f"{email} is a valid")
else:
    print("Invalid email")

