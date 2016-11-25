#! /usr/bin/env python3
# Created on Fri Nov 25 15:06:30 2016
# @author: Edridge D'Souza

import textwrap

def main():
    mystring = input()
    n = int(input())
    
    return textwrap.fill(mystring, n)


if __name__ == '__main__':
    print(main())
 