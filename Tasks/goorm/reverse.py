def reverse(A):
    n, i = len(A), 0
    while i < n//2:
        A[i], A[n-i-1] = A[n-i-1], A[i]
        i += 1


A = list(input())
reverse(A)
print(''.join(str(x) for x in A))

'''
수행시간을 확인해보면 n//2까지 돌기 때문에 O(logn) 시간이 소요된다고 할 수 있다.
'''
