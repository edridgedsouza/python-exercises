def is_leap(year):
    leap = False
    if 1900 <= year <= 10**5:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
    return leap
    
if __name__ == '__main__':
    y = int(input())    
    print(is_leap(y))