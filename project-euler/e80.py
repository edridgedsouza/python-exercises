"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
import decimal # Easiest way to gain precision
decimal.getcontext().prec = 105 # Extra precision

def SumFirstHundred(number):
    dec = list(str(decimal.Decimal(number).sqrt()))
    dec = dec[0:1] + dec[2:] # Exclude the decimal point
    return sum([int(x) for x in dec[:100]])
    


squares = [x ** 2 for x in range(11)] # Exclude the square values to get only irrational
sums = [SumFirstHundred(x) for x in range(1,101) if x not in squares]
print(sums, "\n\n", sum(sums), sep='')