import random

# ascii art uses unicode characters

print("\u25CF \u250C \u2510 \u2502 \u2514 \u2518")
# ● ┌ ┐ │ └ ┘

"┌---------┐"
"│         │"
"│         │"
"│         │"
"└---------┘"

diceArt = {
    1:("┌---------┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└---------┘"),
    2:("┌---------┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└---------┘"),
    3:("┌---------┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└---------┘"),
    4:("┌---------┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└---------┘"),
    5:("┌---------┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└---------┘"),
    6:("┌---------┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└---------┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

print(dice)
# for die in range(num_of_dice):
#     for i in range(5):
#         print(diceArt[dice[die]][i])

# for vertical display
# for die in range(num_of_dice):
#     for line in diceArt.get(dice[die]):
#         # diceArt.get(dice[die]) returns the entire tuple and u can print it one by one
#         print(line)

# for horizontal display
for i in range(5):
    for die in dice:
        print(diceArt.get(die)[i],end=" ")
    print()

for die in dice:
    total+=die
print(f"total : {total}")