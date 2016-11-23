#! /usr/bin/env python3
# Created on Wed Nov 23 15:24:43 2016
# @author: edridge

def main():
    first = input()
    last = input()
    out = 'Hello {} {}! You just delved into python.'.format(first, last)
    return out


if __name__ == '__main__':
    print(main())
 