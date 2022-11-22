#A:배열, tmp, count는 전역변수로


def merge_sort(A, p, r):
  #p=시작 r=끝
    if (p < r and count <= K):
        q = (p + r) // 2 #중간 index 구하기
        merge_sort(A, p, q) #왼쪽 정렬
        merge_sort(A, q + 1, r) #오른쪽 정렬
        merge(A, p, q, r) #두 정렬시킨 것을 합친다


def merge(A, p, q, r):
    global count, result
    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if (A[i] <= A[j]):
          # 인덱스 j의 값이 i깂 보다 크거나 같을 때,
            tmp.append(A[i])
            i += 1
            # i인덱스 것을 넣어준다. (정렬이므로) 그 후 인덱스를 포인트 한다고 할 수있는
            # i를 1증가
        else:
          #반대의 경우
            tmp.append(A[j])
            j += 1

# 남게될 경우
    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

        # 

    i, t = p, 0

#시간초과를 위해 추가한 코드
#k번째 수 찾을 때 return 
    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K: #찾는 값(K번째 수)과 일치할 경우
            result = A[i]
            break
        i += 1
        t += 1


N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
result = -1
merge_sort(A, 0, N - 1)
print(result)
