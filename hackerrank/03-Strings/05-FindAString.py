#! /usr/bin/env python3
# Created on Fri Nov 25 14:46:02 2016
# @author: Edridge D'Souza


def main():
    mainstring = input()
    substring = input()
    
    matches = 0
    for i in range(len(mainstring)):
        if mainstring[i:i+len(substring)] == substring:
            matches += 1
    return matches


if __name__ == '__main__':
    print(main())
 