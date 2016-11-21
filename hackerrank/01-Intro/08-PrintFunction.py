def listUpTo(n):
    return [print(x, end="") for x in range(1, n+1)]
    
if __name__ == '__main__':
    num = int(input())
    listUpTo(num)