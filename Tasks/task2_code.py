import heapq

hsum = 0
S = []  # 최대힙 사용-root인 값 (-붙여서 젤 작은 값이 중요)
M = []
L = []  # 최소힙 사용 -root인 값( heapq에서 제공, 가장 큰 값이 중요)
nums = list(map(int, input().split()))

heapq.heappush(M, nums[0])
hsum += nums[0]
# 가장 첫번째에는 무조건 M에 들어가야하기 때문에

for n in range(1, len(nums)):
    k = n//3
# 가장 첫번째는 for문 밖에서 처리해줬기 때문에 다음번 부터 시작

    if nums[n] > M[0]:
        heapq.heappush(L, nums[n])
    else:
        heapq.heappush(S, -nums[n])

    # 옮기면서 k//3+1 번째 값 찾아내는 부분
    if len(S) > k:
        heapq.heappush(L, heapq.heappop(M))
        heapq.heappush(M, -(heapq.heappop(S)))
        hsum += M[0]

    elif len(S) == k:
        hsum += M[0]

    # elif len(S)<k:
    else:
        heapq.heappush(S, -heapq.heappop(M))
        heapq.heappush(M, heapq.heappop(L))
        hsum += M[0]


print(hsum)
