#!/usr/bin/python
# -*- coding: utf-8 -*-

# My mockery of the is-ten-thousand npm module
# No offense to its creator@https://github.com/james-work-account/is-ten-thousand
# Python always gets the last laugh :)


def isTenThousand(var):
    """A nested if statement that checks if a number is 10000

    USAGE: 
        isTenThousand(100) # must be int/float
        isTenThousand("wrong type") # returns error message
    """

    if type(var) == float or type(var) == int:
        if int == 10000:
            print("Awesome! " + str(var) + " IS TEN THOUSAND!!!")
        else:
            print("NEIN!" + str(var) + " ist nicht zehn tausend!!")
    else:
        print("Come on, you're a python dev! Don't make silly type mistakes like those Javascript weirdos!")
