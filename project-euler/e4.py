"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(number):
    numstring = str(number)
    if numstring == numstring[::-1]:
        return True
    else:
        return False
        
        
def AllPalindromes(digits): # List out all palindromes of n-digit products
    max = 10 ** digits - 1
    min = 10 ** (digits - 1) -1
    palindromeList = []
    for i in range(max, min, -1):
        for j in range(max, min, -1):
            if isPalindrome(i*j):
                palindromeList.append(i*j)
    return(palindromeList)
            
            
print(max(AllPalindromes(3)))