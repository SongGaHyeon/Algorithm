studentNum = list(range(1, 31))
atdNum = []
notAtdNum =[]
# print(studentNum)

for i in range(28):
    num = int(input())
    atdNum.append(num)
# print(atdNum)

for j in studentNum:
    if j not in atdNum:
        notAtdNum.append(j)

notAtdNum.sort()
for k in range(2):
    print(notAtdNum[k], end=" ")