#! /usr/bin/env python3
# Created on Wed Nov 23 14:20:50 2016
# @author: edridge

def main():
    n = int(input())
    if 2 <= n <= 10:
        line = input()
        nums = [int(i) for i in line.split(" ")]
        
        def WithinConstraints(x):
            return -100 <= x <= 100
        
        if all([WithinConstraints(i) for i in nums]):
            nums = list(set(nums)) # Get uniques then convert back for indexing            
            nums.sort()         
            return nums[-2]


if __name__ == '__main__':
    print(main())
 