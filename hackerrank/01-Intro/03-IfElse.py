def main():
    N = int(input().strip())
    if 1 <= N <= 100:
        if N % 2 == 1:
            print("Weird")
        if N % 2 == 0:
            if 2 <= N <= 5:
                print("Not Weird")
            if 6 <= N <= 20:
                print("Weird")
            if N > 20:
                print("Not Weird")
            
if __name__ == '__main__':
    main()