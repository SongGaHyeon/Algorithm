import sys
input = sys.stdin.readline

n = int(input())
arr_o = list(map(int, input().split()))
arr_t = sorted(list(set(arr_o)))
#set 사용 시 중복을 없애줄 수 있다.
dic = {arr_t[i]: i for i in range(len(arr_t))}
# 해당 값의 인덱스만 뽑아준다.

for i in arr_o:
    print(dic[i], end=' ')
