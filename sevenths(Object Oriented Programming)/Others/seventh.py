
# Exceptions - ZeroDivisionError, TypeError and ValueError - they interrupt the flow of a program
# 1/0 - This gives Zero Division Error
# 1+"1" - This gives Type Error
# int("pizza") - This gives Value Error
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero, baka")
except ValueError:
    print("Please enter only numbers")
except Exception:
    print("Something went wrong")
    # This one catches all exception and should be a last resort
finally:
    # Happens regardless of if they are exceptions or not,
    # usually with opening and closing files, u want to ensure u close the files back after
    print("Do Some Cleanup here")
