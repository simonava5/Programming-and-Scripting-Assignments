# Simona Vasiliauskaite
# 02/03/2018
# Project Euler 5

# Exercise 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


i = 1
for x in (range(2, 21)): # all the numbers from 2 to 20
  if i % x > 0: 
    for n in range(2, 21): 
      if (i*n) % x == 0: 
        i *= n 
        break 

print(i)
