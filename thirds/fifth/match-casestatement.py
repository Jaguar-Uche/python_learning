# how other languages use switch case and it is cleaner than plenty if else

def day_of_week(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is monday"
        case 3:
            return "It is tuesday"
        case 4:
            return "It is wednesday"
        case 5:
            return "It is thursday"
        case 6:
            return "It is friday"
        case 7:
            return "It is saturday"
        case _:
            return "Not a valid day"
# underscore is a wildcard and it executes if none of the others get executed
print(day_of_week(0))

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return False

# Since all of them are getting repeated, i can use comma for it

print(is_weekend("Pizza"))