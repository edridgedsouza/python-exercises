def main():
    a = int(input())
    b = int(input())
    string = '{0}\n{1}'.format(a//b, a/b)
    return string
        
        
if __name__ == '__main__':
    print(main())