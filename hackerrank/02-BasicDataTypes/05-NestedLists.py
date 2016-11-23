#! /usr/bin/env python3
# Created on Wed Nov 23 14:32:27 2016
# @author: edridge

def main():
    n = int(input())
    mylist = []
    if 2 <= n <= 5:
        for i in range(2*n):
            mylist.append(input())
        
    # Use a dict because it makes this all easier
    mydict = {mylist[i]:float(mylist[i+1]) for i in range(0,len(mylist), 2)}
    
    def SecondLowest(dictvalues):
        values = list(dictvalues)
        values = list(set(values)) # Uniques
        values.sort()
        return values[1]
    
    names = [name for name, score in mydict.items() if score == SecondLowest(mydict.values())]
    names.sort() # Alphabetize    
    
    out = '\n'.join(names)    
    print(out)

if __name__ == '__main__':
    main()
 