# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# Exercise executed by Simona Vasiliauskaite

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Vasiliauskaite"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Following text is the output for exercise 2 above

# My surname is Vasiliauskaite
# The first letter V is number 86
# The last letter e is number 101
# Fibonacci number 187 is 538522340430300790495419781092981030533

# What does ord() mean? My answer is below
# Like a lot of the students here I didn't know what ord() command meant until I looked it up on Google.
# It makes sense now that all numbers, letters, characters etc have numeric codes and when I looked up the ASCII character set,
# the capital V and lower case e matched the output in visual code.


# Exercise 1 - My name is Simona, so the first and last letter of my name (S + A = 19 + 1) give the number  20.
# The 20th Fibonacci number is 6765. 
