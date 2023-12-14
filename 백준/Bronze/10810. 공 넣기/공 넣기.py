N, M = map(int, input().split())
basket = [0]* N



for i in range(M):
    a, b, c = map(int, input().split())
    for j in range(a-1,b):
        basket[j] = c


print(*basket)

        
