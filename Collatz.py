# Simona Vasiliauskaite 12/02/2018
# Testing Collatz Conjecture


# Definition: The Collatz conjecture is a conjecture 
# in mathematics that concerns a sequence defined
# as follows: start with any positive integer n.
# Then each term is obtained from the previous term
# as follows: if the previous term is even, the next 
# term is one half the previous term.


def collatz_sequence(n):
    num_seq = [n]
    if n < 1:
       return []
    while n > 1:
       if n % 2 == 0: 
         n = int(n / 2) # The formula states that if the number is even, divide it by two
       else:
         n = int(3 * n + 1) # and if the number is odd, triple it and add one    
    return num_seq

print(collatz_sequence(17))

# This process will eventually reach the number 1, regardless of which positive integer is chosen initially.
# I used integer 17 as per assignment.
