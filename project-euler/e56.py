"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

def DigitSum(a,b):
    power = list(str(a ** b))
    return sum([int(x) for x in power])
    
maxsum = 0
for a in range(1, 101):
    for b in range(1, 101):
        maxsum = max(maxsum, DigitSum(a,b))
print(maxsum)