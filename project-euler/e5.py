"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Not particularly elegant, but also introduces a prime factorization algorithm

def PrimeFactorize(x):
    factorlist = []
    for i in range(2, x // 2 + 1):
        while x % i == 0:
            factorlist.append(i)
            x = x / i
    factorlist.append(int(x))
    return factorlist


def LCM(x,y): # Find prime factorization of x and y, then find max-union
    
    # Check whether one is multiple of the other:
    if y % x == 0:
        return y
    elif x % y == 0:
        return x
    
    # If neither are multiples of each other, solve by prime factors
    
    xfact = PrimeFactorize(x)
    yfact = PrimeFactorize(y)
    
    def count(factorlist):
        compositelist = {}
        visitedlist = []
        for i in factorlist:
            if i not in visitedlist:
                visitedlist.append(i)
                compositelist[i] = factorlist.count(i)
        return compositelist # Gives list of prime factors and number of appearances
        
    # Find prime composition of both numbers
    # Then combine dicts by key, such that 
    # {key1: val1, key2: val2} + {key1: val3, key2: val4}
    # becomes
    # {key1: max(val1,val3), key2: max(val2,val4)}
    
    xcount = count(xfact)
    ycount = count(yfact)
    keys = list(xcount.keys()) + list(ycount.keys())
    keys = list(set(keys)) # Only uniques
    
    combined = {}
    
    for key in keys: # Combine factor counts in both x and y by max
        if key in xcount.keys() and key in ycount.keys():
            combined.update({key:max(xcount[key],ycount[key])})
        elif key in xcount.keys():
            combined.update({key:xcount[key]})
        elif key in ycount.keys():
            combined.update({key:ycount[key]})
    
    
    # Take this combined dict, and raise each key to the power of its value   
    product = 1   
    for key, value in combined.items():
        product *= key ** value

    return product
    

lcm = 1
for i in range(1,21): # Behaves well up until 19, then takes very long
    lcm = LCM(lcm, i)    
    print(lcm)       
    