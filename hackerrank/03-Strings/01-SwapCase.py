#! /usr/bin/env python3
# Created on Wed Nov 23 15:13:47 2016
# @author: edridge

def main():
    s = input()
    letters = list(s) # list of letters
    
    def swap(letter):
        if letter.isupper():
            return letter.lower()
        elif letter.islower():
            return letter.upper()
        else:
            return letter
    
    swapped = [swap(l) for l in letters]
    out = ''.join(swapped)
    return out


if __name__ == '__main__':
    print(main())
 