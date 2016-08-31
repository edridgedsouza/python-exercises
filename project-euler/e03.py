"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""



def MaxPrimeFactor(n):
    for i in range(1, n // 2):
        while n % i == 0 and i != 1:    
            n = n // i
            # print(" i" , i, "N" , n) # See algorithm in progress
            if i == n or n==1:
                return i
    
    
print(MaxPrimeFactor(600851475143))