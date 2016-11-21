def main():
    a = int(input())
    b = int(input())
    string = '{0}\n{1}\n{2}'.format(a+b, a-b, a*b)
    if 1 <= a <= 10**10 and 1 <= b <= 10**10:
        return string
        
        
if __name__ == '__main__':
    print(main())