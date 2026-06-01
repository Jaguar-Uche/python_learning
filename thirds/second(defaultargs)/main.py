import time

# default argument for certain parameters, omitted when you

def net_price(list_price, discount=0.0, tax=0.05):
    return list_price * (1-discount) * (1+tax)
# in the parameter name = for a default value

print(net_price(500, 0, 0.05))
print(net_price(500))
# prints the same thing as the one above it cause it takes default value of these things

print(net_price(500,0.1))
print(net_price(500,0.1, 0))

# if I want to call using default second value and a different value for third parameter
print(net_price(500, tax=0.04))

# end comes first cause non default should come before the default one
def count(end,start=15):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    #     time.sleep amount of time to wait before continuing
    print("DONE!")

count(30)