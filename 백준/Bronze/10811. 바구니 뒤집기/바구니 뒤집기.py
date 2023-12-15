N , M = map(int, input().split())
basket = list(range(1,N+1))

for i in range(M):
    a, b = map(int, input().split())
    # slicing 먼저 해서 reverse
    temp = basket[a-1:b]
    temp.reverse()
    basket[a-1:b] = temp

print(*basket)
