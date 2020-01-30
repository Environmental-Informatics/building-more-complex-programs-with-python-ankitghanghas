"""
Created on Sunday Jan 19 2020
by Ankit Ghanghas

Exercise 5.2 ThinkPython

This  code takes 4 integer inputs from the user and tests the validity of feramt's 
theorem using these 4 inputs.
Fermat's Theorem:
    For any input values a, b, c and power n, given n is greater than 2
    
    a^n + b^n = c^n : # ^ indicates raised to power
    

Fermat's Theorem
"""

def check_fermat(a,b,c,n):
    n=int(n)
    if n<=2: # this steps if the power (exponent) specified is greater than 2
        print("Provide n greater than 2")
        return
    if int(a)**n + int(b)**n == int(c)**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that dosen't work")

a=input("Input a integer value of 'a' \n")
b=input("Input a integer value of 'b' \n")
c=input("Input a integer value of 'c' \n")
n=input("Input a integer value of 'n' \n")

check_fermat(a,b,c,n)        