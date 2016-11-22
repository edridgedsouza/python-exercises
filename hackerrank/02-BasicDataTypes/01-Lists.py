#! /usr/bin/env python3
# Created on Tue Nov 22 15:42:18 2016
# @author: edridge

import re

def main():
    mylist = []
    lines = int(input())
    operations = {
    "print" : lambda x: print(x),
    "sort" : lambda x: x.sort(),
    "reverse": lambda x: x.reverse(),
    "pop": lambda x: x.pop(),
    "insert": lambda x: x.insert(i, e),
    "remove": lambda x: x.remove(e),
    "append": lambda x: x.append(e)
    }    
    
    for line in range(lines):
        command = input()
        pattern = re.compile("\w+")
        keyword = re.findall(pattern, command)[0] # First word
        
        if keyword == "insert":
            i = int(re.findall(pattern, command)[1])
            e = int(re.findall(pattern, command)[2])
        if keyword == "remove" or keyword == "append":
            e = int(re.findall(pattern, command)[1])
            
        # Now parse i and e
        
        f = operations[keyword]
        f(mylist)


if __name__ == '__main__':
    main()
