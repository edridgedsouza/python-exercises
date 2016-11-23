#! /usr/bin/env python3
# Created on Wed Nov 23 14:53:05 2016
# @author: edridge

def main():
    n = int(input())
    lines = []
    if 2 <= n <= 10:
        for i in range(n):
            lines.append(input())
    else:
        return 0
    
    lookup = input()
    
    scores = {i.split(" ")[0]: [float(i.split(" ")[1]), 
                                float(i.split(" ")[2]), 
                                float(i.split(" ")[3])]
                                for i in lines}   
    
    def mean(numList):
        return sum(numList)/len(numList)
    
    averages = {key: mean(val) for key, val in scores.items()}
    print("{0:.2f}".format(averages[lookup])) # the .2f means 2 decimal places

if __name__ == '__main__':
    main()
 