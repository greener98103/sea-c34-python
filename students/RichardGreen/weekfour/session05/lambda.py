#!/usr/bin/env python
'''Write a function that returns a list of n functions, such that
each one, when called, will return the input value, incremented by
an increasing number. Use a for loop, a lambda, and a keyword argument
Extra credit:  Do it with a list comprehension, instead of a for loop'''

# Lets create a function that returns a list of functions


def function_builder(num):

    mylist = []
    for i in range(num):
        mylist.append(lambda x, i=i: x + i)
    return mylist

if __name__ == "__main__":

    # Now lets test our function to make sure it works

    # As in the writeup for the assignment

    # so the_list should contain n functions (callables)
    the_list = function_builder(4)

    # the zeroth element of the list: a function that adds 0 to the input
    print(the_list[1](2))

# Lets make some assert statements to unit test our code

    func_test7 = function_builder(7)

    assert func_test7[3](5) == 8

    assert func_test7[4](5) == 9

    assert func_test7[5](5) == 10

    func_test10 = function_builder(10)

    assert func_test10[3](8) == 11

    assert func_test10[4](8) == 12

    assert func_test10[5](10) == 15
