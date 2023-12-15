# 1. 다이얼 숫자당 알파벳을 저장 . 초와 함께
# 2. 시간 계산

# 알고리즘 분류 : 구현

phoneAlpha = {"ABC":3, "DEF":4, "GHI":5, "JKL":6, "MNO":7, "PQRS":8, "TUV":9, "WXYZ":10}
phoneNum = str(input())
cnt = 0

for i in phoneNum:
    for j in phoneAlpha.keys():
        if i in j:
            cnt += phoneAlpha.get(j)

print(cnt)
