def main():
    N = int(input())
    if 1 <= N <= 20:
        nums = [str(i**2) for i in range(N)]
        print('\n'.join(nums))
        
        
if __name__ == '__main__':
    main()