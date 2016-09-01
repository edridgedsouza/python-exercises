"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial

def IsCurious(num):
    numlist = list(str(num))
    facts = [factorial(int(x)) for x in numlist]
    return sum(facts) == num
    
    
def iterate(digits):
    # An n-digit number will be curious if at least 10^(n-1) and at most factorial(9)*n
    # Usually the upper limit is 10^n. Is there a point where n*9! < 10^n?
    # Mathematica says that n*9! and 10^n intersect at 6.36346.
    # Therefore, when you call this function, only iterate from 1-7 digits
    minimum = 10**(digits-1)
    maximum = 10**digits
    curious = [i for i in range(minimum, maximum+1) if IsCurious(i)]
    return curious
    

curiouslist = []  
for i in range(2,8): # Ignore sinle-digit solutions, and go up to 7-digit solutions
        curiouslist.append([x for x in iterate(i)])
        
# Flatten
flatlist = [item for solution in curiouslist for item in solution]
print(flatlist, sum(flatlist))