# concession stand game

menu = {"pizza":3.00,
        "nachos": 4.30,
        "pop corn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total =0
print("--------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f} ")
print("-----------------------")

while True:
    food = input("Select an item(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print(cart)
print("------ YOUR ORDER -------")
if len(cart)>0:
    for food in cart:
        total += menu.get(food)
        print(food, end=" ")
print()
print(f"The total is: ${total:.2f}")