N = int(input())
numList = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(N):
    if(numList[i]==v):
        cnt +=1
    else:
        continue

print(cnt) 
