# Simona Vasiliauskaite
# 16/03/2018
# Exercise 6 - Calculating the factorial of a number


def factorial(n):
    if n == 0: # test that the factorial number isn't 0
        return 1 # if it is, 0 equals to 1
    else:
        return n * factorial(n-1) 
n=int(input("Input a number to calculate the factorial : "))
print(factorial(n))
