#! /usr/bin/env python3
# Created on Thu Dec  1 17:00:46 2016
# @author: Edridge D'Souza
"""It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000)."""
from math import sqrt

def area(sides,base):
    p = (2*sides+base)/2
    triArea = sqrt(p*(p-sides)*(p-sides)*(p-base))
    return triArea

def perim(sides, base):
    return 2*sides + base

def main():
    limit = 1000000000//3
    triangles = [[[a, a - 1], [a,a + 1]] for a in range(2,limit+1)]
    coords = [item for sublist in triangles for item in sublist]
    
    perims = [perim(i[0],i[1]) for i in coords if area(i[0],i[1]) % 1 == 0]
    print(sum(perims))
 
if __name__ == '__main__':
    main()
