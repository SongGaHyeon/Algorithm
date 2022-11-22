def reverse(L, a):
    n = len(L)
    if a < n//2:
        L[a], L[n-a-1] = L[n-a-1], L[a]
        reverse(L, a+1)


L = list(input())
reverse(L, a=0)
print(''.join(str(x) for x in L))

# reversion
# 수행시간은 같은 것 같다. 다만 교수님께서 재귀 시 아주 미세하게 수행시간이 더 크다고 하셨는데
# 일반 reverse가 더 좋을 것 같다.
