
# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to be deposited: "))
    if amount < 0 :
        print("That's not a valid amount")
        return 0
    else:
        return amount

def tax_amount(amount):
    if amount >= 5000:
        print(f"{10 * amount/100} taken as tax")
        return 90 * amount / 100
    elif amount >= 1000:
        print(f"{5 * amount/100} taken as tax")
        return 95 * amount / 100
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance :
        print("Insufficient funds")
        return 0
    elif amount < 0 :
        print("Withdrawal must be greater than or equal to 0")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("***********************")
        print("     Banking Program   ")
        print("***********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount = tax_amount(deposit())
            balance+=amount
            print("*************************")
            print(f"${amount:.2f} deposited to your account")
            show_balance(balance)
            print("*************************")

        elif choice == "3":
            amount = tax_amount(withdraw(balance))
            balance -= amount
            print("*************************")
            print(f"${amount:.2f} withdrawn from your account")
            show_balance(balance)
            print("*************************")
        elif choice == "4":
            is_running = False
        else:
            print("**************************")
            print("That is not a valid choice")
            print("**************************")

    print("*************************")
    print("Thank You have a nice day")
    print("*************************")
if __name__ == "__main__":
    main()