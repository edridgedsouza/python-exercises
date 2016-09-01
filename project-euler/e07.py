"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def ListPrimes(n): # Give nth prime number list
    def IsPrime(x):
        return all(x % i for i in range(2, x //2 + 1)) # StackOverflow helped with this bc I got lazy
    
    primeList = []
    counter = 2 # Don't count 1 as a prime number
    while len(primeList) < n:
        if IsPrime(counter):
            primeList.append(counter)
        counter += (counter % 2 + 1) # Only do even numbers
    return(primeList)
    
print(ListPrimes(10001)[-1])

# Not fast at all but hey, it works