import sys
from collections import Counter


numbers = []
# 입력받을 숫자 갯수 받아서 그 수만큽 num에 받아
# numbers에 append
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()  # 오름차순

cnt = Counter(numbers).most_common(2)

#
print(cnt)
# 최빈값을 위한 코드 부분
# most_common(2)의 숫자 2는 최빈값 2개를 가져오는 것임

print(round(sum(numbers) / len(numbers)))
# 산술평균 (round는 반올림을 위해 사용)

print(numbers[len(numbers) // 2])
# 중앙값: 숫자 개수 홀수이기 때문에 해당 코드로 가능


if len(numbers) > 1:
    # 각수가 몇번 나타나는지가 담겨있음
    # 최빈값이 하나 이상인 경우
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    # 숫자 갯수가 1개보다 작으면 그 값을 print해주는 되는 것이다
    print(cnt[0][0])
print(max(numbers) - min(numbers))
