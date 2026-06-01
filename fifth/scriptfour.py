from scriptthree import *

# We want to borrow something ,but we don't want to run the body of code directly

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script four")
    favorite_food("shawarma")
    favorite_drink("coffee")
    print("Goodbye")

if __name__ == "__main__":
    main()
