import math # Thankfully, comprehensions and map() save us space
N, M = map(int, input().split())
[print(('.|.'*(2*i-1)).center(M, '-')) for i in range(1,math.ceil(N/2))]
print('WELCOME'.center(M, '-'))
[print(('.|.'*(2*i-1)).center(M, '-')) for i in range(math.floor(N/2), 0, -1)]