#! /usr/bin/env python3
# Created on Wed Nov 23 14:09:13 2016
# @author: edridge

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    def DoesNotAdd(q,r,s):
        return not q + r + s == n

    interior = [[a,b,c] for a in range(x+1) 
        for b in range(y+1) 
        for c in range(z+1) 
        if DoesNotAdd(a,b,c)]
        
    print(interior)
    
if __name__ == '__main__':
    main()
 