#! /usr/bin/env python3
# Created on Fri Nov 25 14:41:57 2016
# @author: Edridge D'Souza

def main():
    mystring = input()
    command = input()
    pos = int(command.split(' ')[0])
    letter = command.split(' ')[1]
    
    mystring = list(mystring)
    mystring[pos] = letter
    return ''.join(mystring)


if __name__ == '__main__':
    print(main())
 