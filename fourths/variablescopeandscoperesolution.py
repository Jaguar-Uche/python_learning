
# variable scope is where a variable is visible and accessible
# scope resolution - (LEGB) - Local -> Enclosed -> Global -> Built-in

# variables declared within a function have a local scope

# check for variable locally then check enclosed then check global 

from math import e

def func1():
    a =1
    # a is local to func1
    print(a)
    print(x)
    print(e)
    # this e is 6.7 although the built in e, which was imported is 2.7
    # this is because python checks for the variable globally before checking the built in ones
    def func2():
        b =2
        # b is local to func2
        print(b)
        print(a)
        print(x)
    #     The enclosed version (a) is used
    func2()

x = 4

e = 6.7
# this declares x globally and the functions can access it and print


func1()