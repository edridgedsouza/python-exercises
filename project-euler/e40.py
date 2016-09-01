"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def ConstructNumber(length):
    num = ["."]
    for count in range(1, length+1):
        num.append(str(count))
    num = ''.join(num)
    return num

total = 1
num = ConstructNumber(10**6 + 1)
for i in range(7):
    total *= float(num[10**i])
print(total)