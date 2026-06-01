# Shopping cart program

foods = []
prices = []
total = 0
# We are using lists because they are changeable and tuples aren't

while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower() == "q":
        break
    else :
        foods.append(food)
        price = float(input(f"Enter the price of {food}: "))
        prices.append(price)


for food in foods:
    print(food)

for price in prices:
    print(price)
    total += price

print("----- YOUR CART -----")
for x in range(len(foods)):
    print(f"{foods[x]:10} ",end="")
    print(f"{round(prices[x], 2)}")
    total += prices[x]

print(f"Your total is: {total}")