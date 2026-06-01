#format specifiers allow u to format a value based on string inserted {value:flags}

price_one = 30000000.1959
price_two= -987.65
price_three=12.34

print(f"price one is ${price_one :.3f}")
#rounds the number to 2 decimal place
print(f"price two is ${price_two:.2f}")
print(f"price three is #{price_three:.1f}")
print(f"price one is #{price_one:10}")
#10 means the variable would take up 10 character spaces
print(f"price one is #{price_one:010}")
#variable would take up character space of 10 and the empty spaces would be padded with 0
print(f"price one is #{price_one:<10} helossey")
#justify the variable to the left of the space, the space now appears after it
print(f"price one is #{price_one:>10} helossey")
#justifies the variable to the end of the spaces(this is the default)
print(f"price one is #{price_one:^10} helossey")
#justifies the variable to the center of the spaces
print(f"price one is #{price_one: }")
print(f"price one is #{price_two: }")
print(f"price one is #{price_three: }")
#space means display one space before positive numbers
print(f"price one is #{price_one:+}")
print(f"price one is #{price_two:+}")
print(f"price one is #{price_three:+}")
#space means display plus sign before positive numbers
print(f"price one is #{price_one:,}")
#puts commas after each thousandth place
print(f"price one is #{price_one:+,.2f}")
print(f"price one is #{price_two:+,.2f}")
print(f"price one is #{price_three:+,.2f}")