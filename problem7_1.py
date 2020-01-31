"""
Created on Sunday Jan 19 2020
by Ankit Ghanghas

Exercise 7.1 ThinkPython

This code takes a number a and calculates its apporimate square root 
using Newton's Method and then compare it to the square root output from math package.
The output prints a table of original number, approximated sqrt denoted by mysqrt, 
sqrt fround using the math package and the difference.

"""
import math

def mysqrt(a):
    """
    This funciton estimates the approximate square root of a number r
    """
    x=1.0 # intital estimate of the value of square root
#    epsilon=0.0000001
    while True:
        y= (x+a/x)/2 # iterated estimate of the square root assuming x was correct
        if abs(y-x)==0:     #instead for more appropirate alignment with float inputs i would instead use abs(y-x)<epsilon
            break
        x=y
    return x
def test_square_root(a): # this step creates the print table as specified by the question
    dash = '-'*40
    print('{:<4s}{:^20s}{:^20s}{:<30s}'.format('a','mysqrt(a)','math.sqrt(a)','diff'))
    print(dash)
    for i in range(len(a)):
        print('{:<4.1f}{:<20.12f}{:<20.12f}{:<30s}'.format(a[i],mysqrt(a[i]),math.sqrt(a[i]),str(mysqrt(a[i])-math.sqrt(a[i]))))
# ask for either a list of positive floats or just one value of float as an input
a=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
test_square_root(a)
