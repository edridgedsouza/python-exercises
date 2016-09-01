"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def IsPalindrome(num):
    numstr = str(num)
    return int(numstr[::-1]) == num
    
def binary(num):
    return int(str(bin(num))[2:])

numlist = [x for x in range(1,1000000) if IsPalindrome(x) and IsPalindrome(binary(x))]
print(sum(numlist))