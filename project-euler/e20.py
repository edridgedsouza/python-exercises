"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial # Cheating? It's not THAT hard to implement

def Factorial(x): # Use a capital F is you think importing is cheating
    fact=1
    for i in range(1,x+1):
        fact *= i
    return fact

digits = list(str(Factorial(100)))
print(sum([int(x) for x in digits]))