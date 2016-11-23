#! /usr/bin/env python3
# Created on Wed Nov 23 14:01:17 2016
# @author: edridge

def main():
    n = int(input())
    nextline = input()
    nums = nextline.split(" ")
    if len(nums) == n:
        tup = tuple(int(i) for i in nums)
        return hash(tup)

if __name__ == '__main__':
    print(main())
 