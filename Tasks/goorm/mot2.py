n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
# lambda를 이용한 sort방법은 최악의 경우에 O(nlogn) 시간이 보장된다.

mot = 1
ans = arr[0][1]
# 막대의 오른쪽 끝점을 ans에 저장


for i in range(1, n):
    # n만큼 반복적으로 비교하여 ans보다 다음 막대의 왼쪽 끝값이 더 크다면 ans를 그 값의 오른쪽 끝 값으로 초기화 해주고 못의 개수를 증가시켜준다
    if (ans < arr[i][0]):
        ans = arr[i][1]
        mot += 1

    else:
        continue

print(mot)


'''
O(nlogn)의 수행시간이 소요된다. 
for문에서는 O(n)의 수행시간이 걸리며, 람다 정렬식에서는 O(nlogn)이 걸리기 때문에 
총 O(nlogn) 수행시간이 소요됨을 알 수 있다.
'''
