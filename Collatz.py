# Simona Vasiliauskaite 12/02/2018
# Testing Collatz Conjecture

def collatz_sequence(n):
    num_seq = [n]
    if n < 1:
       return []
    while n > 1:
       if n % 2 == 0: 
         n = int(n / 2) # The formula states that if the number is even, divide it by two
       else:
         n = int(3 * n + 1) # and if the number is odd, triple it and add one
       num_seq.append(n)    
    return num_seq

print(collatz_sequence(17))

# This process will eventually reach the number 1, regardless of which positive integer is chosen initially.
# I used integer 17 as per assignment.
