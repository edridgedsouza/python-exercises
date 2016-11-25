#! /usr/bin/env python3
# Created on Fri Nov 25 14:52:05 2016
# @author: Edridge D'Souza

def main():
    S = input()
    
    def Validate(s):
        a = [i.isalnum() for i in s]
        b = [i.isalpha() for i in s]
        c = [i.isdigit() for i in s]
        d = [i.islower() for i in s]
        e = [i.isupper() for i in s]
        
        return any(a), any(b), any(c), any(d), any(e)

    r = [str(i) for i in Validate(S)] # Results to string
    print('\n'.join(r))

if __name__ == '__main__':
    main()
 