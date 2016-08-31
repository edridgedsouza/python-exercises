"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def SumSquares(n):
    return(sum([x**2 for x in range(1, n+1)]))
    
def SquareSums(n):
    sums = sum([x for x in range(1, n+1)])
    return sums ** 2
    
print(abs(SumSquares(100) - SquareSums(100))) # Wow, it was really that straightforward