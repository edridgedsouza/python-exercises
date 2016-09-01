"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def Collatz(start):
    path = [start]
    while path[-1] != 1:
        if path[-1] % 2 == 0:
            path.append(path[-1] // 2)
        else:
            path.append(path[-1] * 3 + 1)
    return path

def Sieve(maximum):
    filtered = []
    longest = []
    maxLength = 0
    for i in range(1, maximum):
        if i not in filtered:
            coll = Collatz(i)
            if len(coll) > maxLength:
                longest = coll
                filtered.append([x for x in coll if x <= maximum and x not in filtered]) # Add unique values to our skip list
                maxLength = max(maxLength, len(coll))
    return longest, maxLength


print(Sieve(1000000))