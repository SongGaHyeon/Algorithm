# 하노이탑 이동 

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        #하나일 경우 더 경우를 늘려줄 필요가 업다
        return

# 재귀함수 사용
# start와 end만 알고 나머지 막대의 번호는 모름
# 막대의 합이 6
#6에서 아는 번호들을 빼주면 모르는 번호를 알 수 있다

# 시작 막대에서 나머지 한 막대로 n-1개 옮겨준다
    hanoi_tower(n-1, start, 6-start-end)  # 1단계
    print(start, end)  # 2단계
    #남은 것을 시작막대에서 마지막 막대로 .
    hanoi_tower(n-1, 6-start-end, end)  # 3단계
# n-1개를 번호를 모르던 막대에서 마지막 막대로 옮겨준다

n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
