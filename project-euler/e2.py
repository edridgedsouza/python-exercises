"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def Fib(max): # Return a list of even fibbonacci terms less than `max`
    fiblist = []
    if 0 <= max <= 1:
        return max
    else:
        fib1 = 0
        fib2 = 1
        fibbo = 0
        while fib1 + fib2 < max:
            fib1 = fib2
            fib2 = fibbo
            if fibbo % 2 == 0:
                fiblist.append(fibbo)
            fibcum = fib1 + fib2
            if fibcum < max:
                fibbo = fibcum
    return fiblist
    
print(sum(Fib(4000000)))
