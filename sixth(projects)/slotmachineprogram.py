import random
# Python Slot Machine

def spin_row():
    # generate 3 random symbols and put them in a list
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for symbol in range(3)]
#     for every iteration in range 3, return a random symbol


def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
#     Join each element of your List by a space

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[0] =="🍉":
            return bet*4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] =="🔔":
            return bet*10
        elif row[0] =="⭐":
            return bet*20
    return 0

def main():
    balance = 100
    print("***********************")
    print("Welcome to Python Slots")
    print("***********************")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("***********************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid amount.")
            # It skips this iteration and starts afresh
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        payout = get_payout(row,bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round")
        balance+=payout
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again != "Y":
            break
    print()
    print("********************************************")
    print(f"Game Over! Your final balance is ${balance}")
    print("********************************************")

if __name__ == '__main__':
    main()