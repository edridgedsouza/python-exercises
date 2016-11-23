#! /usr/bin/env python3
# Created on Wed Nov 23 15:20:11 2016
# @author: edridge

def main():
    s = input()
    words = s.split(' ')
    return '-'.join(words)


if __name__ == '__main__':
    print(main())
 