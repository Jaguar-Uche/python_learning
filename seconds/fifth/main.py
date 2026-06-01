#nested loop - A loop within a loop

#for print, end is usually a new line character, that's why next characters jump to the next line
for x in range(3):
    for y in range(1, 10):
        print(y, end="")#leaves no space after(removes the next line end and makes it end with no string
    print("\n")
    #print("\n") gives two lines space(one is empty)
    # and your code starts from the next one. because print has default end of \n new line
    # so there are two new lines

height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
value = input("Enter what the rectangle is made of: ")

for x in range(height):
    for y in range(width):
        print(value, end=" ")#leaves a space after each 
    print()

