"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# Use a sieve rather than a recursive function

def ListPrimes(maximum): # Give primes below a number
    excluded = [1]    
    for i in range(2, maximum // 2 + 1):
        counter = 1
        while i*counter <= maximum:
            if i*counter not in excluded and counter > 1: 
                excluded.append(i*counter)
            counter += 1
    return [x for x in range(maximum) if x not in excluded]
    

    
#print(ListPrimes(2000000))

print(sum(ListPrimes(2000000)))