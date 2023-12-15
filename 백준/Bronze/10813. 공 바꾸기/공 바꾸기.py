N, M = map(int, input().split())
ballNum = list(range(1,N+1))

for i in range(M):
    a , b = map(int, input().split())
    c = ballNum[a-1]
    ballNum[a-1] = ballNum[b-1]
    ballNum[b-1] = c
print(*ballNum)
    