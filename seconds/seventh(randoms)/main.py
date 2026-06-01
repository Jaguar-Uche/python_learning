import random

# print(help(random))

# for random whole number randint(range) inclusive
number = random.randint(1,6)
print(number)

low = 1
high = 100

number_two = random.randint(low, high)
print(number_two)

#For a random floating point
number_three = random.random()
print(number_three)

options = ("rock", "paper", "scissor")

option = random.choice(options)
#makes a random choice from this collection

print(option)

cards = ["2","3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)
#to shuffle a collection
print(cards)

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)

guesses = 0
is_running = True

print("Python number guessing game... ")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        if lowest_number <= guess <= highest_number:
            guesses += 1
            if guess < answer:
                print("Too low, try again")
            elif guess > answer:
                print("Too high, try again")
            else :
                print(f"The answer was {answer}")
                print(f"It took you {guesses} guesses")
                is_running = False
            pass
        else:
            print("Invalid guess")
            print(f"Select a number between {lowest_number} and {highest_number}")
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_number} and {highest_number}")