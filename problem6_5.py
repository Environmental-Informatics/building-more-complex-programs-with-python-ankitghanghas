"""
Created on Sunday Jan 19 2020
by Ankit Ghanghas

Exercise 6.5 Think Python

This code asks the user to give two positive integer values and the returns the
Greatest Common Divisor (GCD) for those two numbers.
"""

def gcd(a,b):
    a=int(a) # int(a) converts the input strings'a' to integer
    b=int(b)
    if b>a:  # this conditon checks if the second number is greater that the first one
        a,b=b,a # swaps the two numbers such that first number is now bigger
    if b==0 :
        return a # specifies the base case for the iterations
    else:
        r=a%b # calculates the remainder r when a is divided by b
        return gcd(b,r)

a=input("Input a integer value of 'a' \n")
b=input("Input a integer value of 'b' \n")
print('GCD =', gcd(a,b))