#! /usr/bin/env python3
# Created on Fri Nov 25 15:58:22 2016
# @author: Edridge D'Souza

def main():
    def MakeRow(n, nmax):
        
        
        length = len('{:b}'.format(nmax))
        
        binary = '{:b}'.format(n).rjust(length)
        octal = '{:o}'.format(n).rjust(length)
        hexadecimal = '{:X}'.format(n).rjust(length)
        n = str(n).rjust(length)
        
        # No idea why, but the website wants it this way apparently.
        print('{} {} {} {}'.format(n, octal, hexadecimal, binary))
        
    
    num = int(input())
    [MakeRow(i, num) for i in range(1, num + 1)]


if __name__ == '__main__':
    main()
 