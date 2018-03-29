# Simona Vasiliauskaite
# 16/03/2018
# Exercise 6 - Calculating the factorial of a number

# Definition - Factorial of a number is 
# calculated by multiplying it with all the numbers 
# below it starting from 1.


def factorial(n):
    if n == 0: # test that the factorial number isn't 0
        return 1 # if it is, 0 equals to 1
    else:
        return n * factorial(n-1) # multiply the number with all the numbers below it start from 1.
n=int(input("Input a number to calculate the factorial : ")) 
print(factorial(n))

# the factorial of a number 5 is 120
# the factorial of a number 7 is 5040
# the factorial of a number 10 is 3628800
