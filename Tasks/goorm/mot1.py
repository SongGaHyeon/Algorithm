n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
# 입력으로 받은 배열을 뒷 과정을 위해 미리 정렬해둔다
arr.sort(key=lambda x: x[0])
# lambda를 이용해 2차원 배열의 뒷 값을 정렬한 뒤 다시 앞에 대해서도 정렬한다
lst, ans = [], [1]
# ans에 1을 넣어준 이유는 맨 처음 값 (lst의 0번째 값은 왼쪽 끝 값이기 때문에 eventpoint의 조건에 따라 1은 미리 넣어준다)


def solve(arr):
    j = 0
    i = 1
    lst.append([arr[0][0], 1])
    # arr의 가장 첫번째로 받은 막대기의 왼쪽 값을 넣어둔다.
    # 2차원 배열의 구조로 1을 함께 넣어준 이유는 왼쪽 값/ 오른쪽 값을 구분하기 위해서이다.
    # 이 코드에서 왼쪽 끝 값은 2차원 배열의 [?][1] 로 표현되며 이는 왼쪽 이벤트 포인트 임을 보여준다

    while (i < n):
        # i와 j를 비교하며 새로운 lst 리스트에 넣어준다. 왼쪽 값들은 i를 통해 순차적으로 확인해준다,
        # j는 오른쪽 값들을 순차적으로 확인해준다. 여기서 왼쪽값이란, 구간의 왼쪽 끝 점, 오른쪽 값은 오른			쪽 끝 점을 의미한다.

        # 이 부분에서는 모든 값들을 오름차순으로 정렬되도록 한다. 단, 왼쪽 끝 점인지 오른쪽 끝 점인지에 따라 하나의 못으로 꽂을 수 있는 최대 막대의 개수를 세는 것이 달라진다. 따라서 점을 구분하는 숫자 0,1과 함께 lst에 append 해준다.

        # 정렬하는 우선순위는 1.왼쪽 값 먼저 2. 작은값 먼저 이다.
        if (arr[i][0] <= arr[j][1]):  # 최근 초기화된 오른쪽 끝 점이 왼쪽 끝점보다 크거나 같을 경우
            lst.append([arr[i][0], 1])
            i += 1

        elif (arr[i][0] > arr[j][1]):  # 최근 초기화된 왼쪽 끝 점이 오른쪽 끝 점보다 작을 경우
            lst.append([arr[j][1], 0])
            j += 1

    while (j < n):
        # i가 n까지 확인되고 남은 값들을 lst에 추가하는 과정
        lst.append([arr[j][1], 0])
        j += 1

    lst.sort(key=lambda x: x[0])
    # 정렬되지 않은 소수의 값들을 정렬해주기 위한 부분
    # print(len(lst))
    for i in range(1, len(lst)):
        # lst에서 왼쪽 끝 점일 경우+1, 오른쪽 끝 점일 경우 -1을 해준다
        cnt = ans[i-1]
        if (lst[i][1] == 1):
            ans.append(cnt+1)
        else:
            ans.append(cnt-1)
    return max(ans)
# 최대 값을 return 해준다 ( 최대 값은 하나의 못으로 꽂을 수 있는 최대 막대 개수를 뜻한다 )


print(solve(arr))


'''
정렬 라이브러리는 최악의 경우에도 O(nlogn)의 수행시간을 보장한다.
코드 자체는 O(2n+len(lst))이다. len(lst)는 보통 입력으로 들어온 n의 2배이다.
따라서 O(nlogn)의 수행시간이 걸린다고 할 수 있다.


'''
