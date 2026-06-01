import random

options = ("rock", "paper", "scissors")
running = True
# pick a random choice from options
# If you set your while loop to be true for long codes, it is difficult to track where u break out
# so use booleans instead so you can find the name easily and find where u break out
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice(rock, paper,scissors): ")
    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "rock" and computer == "paper":
        print("You Lose!")
    elif player == "paper" and computer == "scissors":
        print("You Lose!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "rock":
        print("You Lose!")
    else:
        print("You win!")

    if not input("play again? (y/n): ").lower().startswith("y"):
        break
print("Thanks for playing")
# this is better(much shorter than ur code)
# if player == computer:
#     print("It's a tie!")
# elif player == "rock" and computer == "scissors":
#     print("You Win!")
# elif player == "paper" and computer == "rock":
#     print("You Win!")
# elif player == "scissors" and computer == "paper":
#     print("You Win!")
# else:
#     print("You Lose!")